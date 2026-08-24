"""
Metaclass are used to modify a class as it is being created at runtime.
This module shows how a metaclass can add database attributes and tables
to "logic-free" model classes for the developer.
"""

from abc import ABC
from typing import Any


class ModelMeta(type):
    """Model metaclass.

    By studying how SQLAlchemy and Django ORM work under the hood, we can see
    a metaclass can add useful abstractions to class definitions at runtime.
    That being said, this metaclass is a toy example and does not reflect
    everything that happens in either framework. Check out the source code
    in SQLAlchemy and Django to see what actually happens:

    https://github.com/sqlalchemy/sqlalchemy
    https://github.com/django/django

    The main use cases for a metaclass are (A) to modify a class before
    it is visible to a developer and (B) to add a class to a dynamic registry
    for further automation.

    Do NOT use a metaclass if a task can be done more simply with class
    composition, class inheritance or functions. Simple code is the reason
    why Python is attractive for 99% of users.

    For more on metaclass mechanisms, visit the link below:

    https://realpython.com/python-metaclasses/
    """

    # Model table registry
    tables: dict[str, "ModelTable"] = {}
    model_name: str | None
    model_fields: dict[str, "BaseField"]
    model_table: "ModelTable" | None

    def __new__(mcs, name: str, bases: tuple[type, ...], attrs: dict[str, Any]) -> "ModelMeta":
        """Factory for modifying the defined class at runtime.

        Here are the following steps that we take:

        1. Get the defined model class
        2. Add a model_name attribute to it
        3. Add a model_fields attribute to it
        4. Add a model_table attribute to it
        5. Link its model_table to a registry of model tables
        6. Return the modified model class
        """
        kls = super().__new__(mcs, name, bases, attrs)

        # Abstract model does not have a `model_name` but a real model does.
        # We will leverage this fact later on this routine
        if attrs.get("__abstract__") is True:
            kls.model_name = None
        else:
            custom_name = attrs.get("__table_name__")
            default_name = kls.__name__.replace("Model", "").lower()
            kls.model_name = custom_name if custom_name else default_name

        # Ensure abstract and real models have fields so that
        # they can be inherited
        kls.model_fields = {}

        # Fill model fields from the parent classes (left-to-right)
        for base in bases:
            if isinstance(base, ModelMeta):
                kls.model_fields.update(base.model_fields)

        # Fill model fields from itself. Each field is "late bound" to its
        # declared attribute name here: the field object had no name when it
        # was constructed, so we hand it the name at class creation time
        for field_name, field_obj in attrs.items():
            if isinstance(field_obj, BaseField):
                kls.model_fields[field_name] = field_obj.bind(field_name)

        # Register a real table (a table with valid `model_name`) to
        # the metaclass `table` registry. After all the tables are
        # registered, the registry can be sent to a database adapter
        # which uses each table to create a properly defined schema
        # for the database of choice (i.e. PostgresSQL, MySQL)
        if kls.model_name:
            kls.model_table = ModelTable(kls.model_name, kls.model_fields)
            ModelMeta.tables[kls.model_name] = kls.model_table
        else:
            kls.model_table = None

        return kls

    @property
    def is_registered(cls) -> bool:
        """Check if the model's name is valid and exists in the registry."""
        return bool(cls.model_name and cls.model_name in cls.tables)


class ModelTable:
    """Model table."""

    def __init__(self, table_name: str, table_fields: dict[str, "BaseField"]) -> None:
        self.table_name = table_name
        self.table_fields = table_fields
        self.primary_key = next(
            (field_name for field_name, field in table_fields.items() if field.primary_key),
            None,
        )

    def ddl(self) -> str:
        """Build a simple CREATE TABLE statement for the schema."""
        columns = []
        for field_name, field in self.table_fields.items():
            sql = field.column_definition(field_name)
            if field.primary_key:
                sql = f"{sql} PRIMARY KEY"
            if field.default is not None and not field.primary_key:
                sql = f"{sql} DEFAULT {field.default!r}"
            if not field.nullable and not field.primary_key:
                sql = f"{sql} NOT NULL"
            columns.append(sql)
        return f"CREATE TABLE {self.table_name} ({', '.join(columns)});"


class BaseField(ABC):
    """Base field.

    A field carries its declared attribute name in `name`. It does not
    know that name until the metaclass calls `bind` at class creation
    time, which is the classic "late binding" metaclass trick.
    """

    name: str | None
    primary_key: bool
    nullable: bool
    default: Any

    def __init__(self, *, primary_key: bool = False, nullable: bool = True, default: Any = None) -> None:
        self.primary_key = primary_key
        self.nullable = nullable
        self.default = default

    def bind(self, name: str) -> "BaseField":
        """Bind this field to its declared attribute name at runtime."""
        self.name = name
        return self

    def column_definition(self, field_name: str) -> str:
        """Return the column SQL definition for this type."""
        raise NotImplementedError


class CharField(BaseField):
    """Character field."""

    max_length: int

    def __init__(self, *, max_length: int = 255, primary_key: bool = False, nullable: bool = True, default: Any = None) -> None:
        super().__init__(primary_key=primary_key, nullable=nullable, default=default)
        self.max_length = max_length

    def column_definition(self, field_name: str) -> str:
        return f"{field_name} VARCHAR({self.max_length})"


class IntegerField(BaseField):
    """Integer field."""

    def __init__(self, *, primary_key: bool = False, nullable: bool = True, default: Any = None) -> None:
        super().__init__(primary_key=primary_key, nullable=nullable, default=default)

    def column_definition(self, field_name: str) -> str:
        return f"{field_name} INTEGER"


class BaseModel(metaclass=ModelMeta):
    """Base model.

    Notice how `ModelMeta` is injected at the base class. The base class
    and its subclasses will be processed by the method `__new__` in the
    `ModelMeta` class before being created.

    In short, think of a metaclass as the creator of classes. This is
    very similar to how classes are the creator of instances.
    """

    __abstract__ = True  # This is NOT a real table
    row_id = IntegerField(primary_key=True)


class UserModel(BaseModel):
    """User model."""

    __table_name__ = "user_rocks"  # This is a custom table name
    username = CharField()
    password = CharField()
    age = CharField()
    sex = CharField()


class AddressModel(BaseModel):
    """Address model."""

    user_id = IntegerField()
    address = CharField()
    state = CharField()
    zip_code = CharField()


def main() -> None:
    # Real models are given a name at runtime with `ModelMeta`
    assert UserModel.model_name == "user_rocks"
    assert AddressModel.model_name == "address"

    # Real models are given fields at runtime with `ModelMeta`
    assert "row_id" in UserModel.model_fields
    assert "row_id" in AddressModel.model_fields
    assert "username" in UserModel.model_fields
    assert "address" in AddressModel.model_fields

    # Each field is late-bound to its declared attribute name at runtime
    assert UserModel.model_fields["username"].name == "username"
    assert UserModel.model_fields["password"].name == "password"
    assert AddressModel.model_fields["state"].name == "state"

    # Inherited fields keep the name they were bound with in the base class
    assert UserModel.model_fields["row_id"].name == "row_id"
    assert AddressModel.model_fields["row_id"].name == "row_id"

    # Primary keys are tracked on the field and the generated table metadata
    assert UserModel.model_fields["row_id"].primary_key is True
    assert AddressModel.model_fields["row_id"].primary_key is True
    assert UserModel.model_table is not None
    assert AddressModel.model_table is not None
    assert UserModel.model_table.primary_key == "row_id"
    assert AddressModel.model_table.primary_key == "row_id"

    # A field built by hand and not yet bound has no name yet
    assert IntegerField().name is None

    # Char fields can carry a max length, which is used in generated SQL
    username_field = UserModel.model_fields["username"]
    address_field = AddressModel.model_fields["address"]
    assert isinstance(username_field, CharField)
    assert isinstance(address_field, CharField)
    assert username_field.max_length == 255
    assert address_field.max_length == 255

    # Real models have a `ModelTable` that can be used for DB setup
    assert isinstance(ModelMeta.tables[UserModel.model_name], ModelTable)
    assert isinstance(ModelMeta.tables[AddressModel.model_name], ModelTable)

    # A table can generate a simple CREATE TABLE statement from its fields
    assert UserModel.model_table is not None
    assert AddressModel.model_table is not None
    assert (
        UserModel.model_table.ddl()
        == "CREATE TABLE user_rocks (row_id INTEGER PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), age VARCHAR(255), sex VARCHAR(255));"
    )
    assert (
        AddressModel.model_table.ddl()
        == "CREATE TABLE address (row_id INTEGER PRIMARY KEY, user_id INTEGER, address VARCHAR(255), state VARCHAR(255), zip_code VARCHAR(255));"
    )

    # Base model is given special treatment at runtime
    assert not BaseModel.is_registered
    assert BaseModel.model_name is None
    assert BaseModel.model_table is None

    # Every model is created by `ModelMeta`
    assert isinstance(BaseModel, ModelMeta)
    assert all(isinstance(model, ModelMeta) for model in BaseModel.__subclasses__())

    # And `ModelMeta` is created by `type`
    assert isinstance(ModelMeta, type)

    # And `type` is created by `type` itself
    assert isinstance(type, type)

    # And everything in Python is an object!
    assert isinstance(BaseModel, object)
    assert isinstance(ModelMeta, object)
    assert isinstance(type, object)
    assert isinstance(object, object)


if __name__ == "__main__":
    main()
