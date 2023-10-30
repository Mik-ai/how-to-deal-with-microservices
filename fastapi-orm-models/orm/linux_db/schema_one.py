from orm.type_helper import TypeHelper


class CategoriesDimensions:
    __tablename__ = "categories_dimensions"
    __table_args__ ={"schema": "shema1"}

    description_category_id = {
        "type_str": TypeHelper.INTEGER,
        "mapped_column_dict": {"primary_key": True},
    }
    description_category_name = {"type_str": TypeHelper.TEXT}
    weight_min = {"type_str": TypeHelper.INTEGER}
    weight_max = {"type_str": TypeHelper.INTEGER}
    width_min = {"type_str": TypeHelper.INTEGER}
    width_max = {"type_str": TypeHelper.INTEGER}
    height_min = {"type_str": TypeHelper.INTEGER}
    height_max = {"type_str": TypeHelper.INTEGER}
    depth_min = {"type_str": TypeHelper.INTEGER}
    depth_max = {"type_str": TypeHelper.INTEGER}
    parent_id = {"type_str": TypeHelper.INTEGER}
