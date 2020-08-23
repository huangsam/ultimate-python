from abc import ABC


class ModelMeta(type):
    """Model metaclass.

    By studying how SQLAlchemy and Django ORM work under the hood, we can see
    how one may create a rudimentary meta-class for adding useful abstractions
    to class definitions at runtime.

    Two of the main use cases for a metaclass are to (A) modify a class before
    it is visible to a developer and (B) add a class to a dynamic registry for
    further automation.

    For more on meta-classes, feel free to visit the link below:

    https://realpython.com/python-metaclasses/
    https://docs.python.org/3/reference/datamodel.html
    """

    # Model table registry
    tables = {}

    def __new__(mcs, name, bases, attrs):
        """Factory for modifying the defined class at runtime."""
        kls = super().__new__(mcs, name, bases, attrs)

        # Abstract model does not have a `model_name` but a real model does.
        # We will leverage this fact later on this routine.
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

        # Add model fields of its own last
        kls.model_fields.update({
            field_name: field_obj
            for field_name, field_obj in attrs.items()
            if isinstance(field_obj, BaseField)
        })

        # Register a real table (a table with valid `model_name`) to
        # the metaclass `table` registry so that it can be sent later to a
        # database adapter which uses each table entry to create a
        # corresponding physical table in a database.
        if kls.model_name:
            ModelMeta.tables[kls.model_name] = ModelTable(kls.model_name,
                                                          kls.model_fields)

        # Return newly modified class
        return kls


class ModelTable:
    """Model table."""

    def __init__(self, table_name, table_fields):
        self.table_name = table_name
        self.table_fields = table_fields

    def __repr__(self):
        return f"<ModelTable name={self.table_name}>"


class BaseField(ABC):
    """Base field."""

    def __repr__(self):
        """Brief representation of any field."""
        return f"<{type(self).__name__}>"


class CharField(BaseField):
    """Character field."""


class IntegerField(BaseField):
    """Integer field."""


class BaseModel(metaclass=ModelMeta):
    """Base model."""
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
    # Each model was modified at runtime with ModelMeta
    for real_model in BaseModel.__subclasses__():
        print("Real table", real_model.model_name)
        print("Real fields", real_model.model_fields)

    # Each models was registered at runtime with ModelMeta
    for meta_table in ModelMeta.tables.values():
        print("Meta table", meta_table)

    # Base model was given special treatment, as expected
    assert BaseModel.model_name is None


if __name__ == '__main__':
    main()
