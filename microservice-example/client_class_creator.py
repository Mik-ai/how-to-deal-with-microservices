from sqlalchemy.orm import mapped_column, DeclarativeBase
from sqlalchemy.orm.attributes import InstrumentedAttribute

from sqlalchemy.dialects.postgresql import (
    TEXT,
    TIMESTAMP,
    NUMERIC,
    DOUBLE_PRECISION,
    BOOLEAN,
    INTEGER,
    ARRAY,
    VARCHAR,
)


class Base(DeclarativeBase):
    pass


DB_TYPES_DICT = {
    "TEXT": TEXT,
    "TIMESTAMP": TIMESTAMP,
    "NUMERIC": NUMERIC,
    "DOUBLE_PRECISION": DOUBLE_PRECISION,
    "BOOLEAN": BOOLEAN,
    "INTEGER": INTEGER,
    "ARRAY": ARRAY,
    "VARCHAR": VARCHAR,
}


def create_annotated(
    type_str: str,
    mapped_column_dict: dict = {},
) -> InstrumentedAttribute:
    """creating mapped_collumn() for each field

    Args:
        type_str (str): DB type, we use postgresql
        mapped_column_dict (dict, optional): dict for unpacking in mapped_column()

    Returns:
        InstrumentedAttribute: sqlalchemy attribute
    """
    positional_args = []
    if column_name := mapped_column_dict.get("column_name", False):
        positional_args.append(column_name)
    positional_args.append(DB_TYPES_DICT[type_str])
    result = mapped_column(*positional_args, **mapped_column_dict)
    return result


def process_orm_model(orm_model: dict, module):
    """creating an anonymous class and replacing the declared one

    Args:
        orm_model (dict): orm model structure
        module (python module): module where orm models are declared.
    """
    model_name = orm_model.pop("model_name")
    orm_model_fields = {
        key: create_annotated(**value)
        for key, value in orm_model.items()
        if "__" not in key
    }
    for k, v in orm_model.items():
        if "__" in k:
            orm_model_fields[k] = v

    model = type(model_name, (Base,), orm_model_fields)

    setattr(module, model_name, model)
