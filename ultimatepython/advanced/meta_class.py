from abc import ABC


class ModelMeta(type):
    """Model metaclass.

    By studying how SQLAlchemy and Django ORM work under the hood, we can see
    a metaclass can add useful abstractions to class definitions at runtime.
    That being said, this metaclass is a toy example and does not reflect
    everything that happens in either framework.

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
    tables = {}

    def __new__(mcs, name, bases, attrs):
        """Factory for modifying the defined class at runtime."""
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
            kls.model_fields.update(base.model_fields)

        # Fill model fields from itself
        kls.model_fields.update({
            field_name: field_obj
            for field_name, field_obj in attrs.items()
            if isinstance(field_obj, BaseField)
        })

        # Register a real table (a table with valid `model_name`) to
        # the metaclass `table` registry. After all the tables are
        # registered, the registry can be sent to a database adapter
        # which uses each table to create a properly defined schema
        # for the database of choice (i.e. PostgreSQL, MySQL)
        if kls.model_name:
            kls.model_table = ModelTable(kls.model_name, kls.model_fields)
            ModelMeta.tables[kls.model_name] = kls.model_table
        else:
            kls.model_table = None

        # Return newly modified class
        return kls

    @property
    def is_registered(cls):
        """Check if the model's name is valid and exists in the registry."""
        return cls.model_name and cls.model_name in cls.tables


class ModelTable:
    """Model table."""

    def __init__(self, table_name, table_fields):
        self.table_name = table_name
        self.table_fields = table_fields


class BaseField(ABC):
    """Base field."""


class CharField(BaseField):
    """Character field."""


class IntegerField(BaseField):
    """Integer field."""


class BaseModel(metaclass=ModelMeta):
    """Base model.

    Notice how `ModelMeta` is injected at the base class. The base class
    and its subclasses will be processed by the method `__new__` in the
    `ModelMeta` class before being created.

    In short, think of a metaclass as the creator of classes. This is
    very similar to how classes are the creator of instances.
    """
    __abstract__ = True  # This is NOT a real table
    row_id = IntegerField()


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


def main():
    # Real models are given a name at runtime with `ModelMeta`
    assert UserModel.model_name == "user_rocks"
    assert AddressModel.model_name == "address"

    # Real models are given fields at runtime with `ModelMeta`
    assert "row_id" in UserModel.model_fields
    assert "row_id" in AddressModel.model_fields
    assert "username" in UserModel.model_fields
    assert "address" in AddressModel.model_fields

    # Real models are registered at runtime with `ModelMeta`
    assert UserModel.is_registered
    assert AddressModel.is_registered

    # Real models have a `ModelTable` that can be used for DB setup
    assert isinstance(ModelMeta.tables[UserModel.model_name], ModelTable)
    assert isinstance(ModelMeta.tables[AddressModel.model_name], ModelTable)

    # Base model is given special treatment at runtime
    assert not BaseModel.is_registered
    assert BaseModel.model_name is None
    assert BaseModel.model_table is None

    # Every model is created by `ModelMeta`
    assert isinstance(BaseModel, ModelMeta)
    assert all(isinstance(model, ModelMeta)
               for model in BaseModel.__subclasses__())

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
