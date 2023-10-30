from orm.type_helper import TypeHelper

{"type_str": TypeHelper.BOOLEAN}


class Categories:
    __tablename__ = "categories"
    __table_args__ ={"schema": "schema2"}

    category_id = {
        "type_str": TypeHelper.INTEGER,
        "mapped_column_dict": {"primary_key": True},
    }
    name = {"type_str": TypeHelper.TEXT}
    level = {"type_str": TypeHelper.INTEGER}
    slug = {"type_str": TypeHelper.TEXT}
    path = {"type_str": TypeHelper.TEXT}
    is_leaf = {"type_str": TypeHelper.BOOLEAN}
    is_adult = {"type_str": TypeHelper.BOOLEAN}
    icon = {"type_str": TypeHelper.TEXT}
    page = {"type_str": TypeHelper.INTEGER}
