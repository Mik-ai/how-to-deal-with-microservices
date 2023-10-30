from orm.type_helper import TypeHelper


class SomeTable:
    __tablename__ = "this_is_db_table_1"

    marketplace_id = {
        "type_str": TypeHelper.INTEGER,
        "mapped_column_dict": {"primary_key": True},
    }
    offer_id = {"type_str": TypeHelper.TEXT}
    product_id = {"type_str": TypeHelper.INTEGER}
    created_at = {"type_str": TypeHelper.TIMESTAMP}
    group_name = {"type_str": TypeHelper.TEXT}
    state = {"type_str": TypeHelper.TEXT}
    state_name = {"type_str": TypeHelper.TEXT}
    validation_state = {"type_str": TypeHelper.TEXT}
    state_description = {"type_str": TypeHelper.TEXT}
    item_errors = {"type_str": TypeHelper.BOOLEAN}
    box_height = {"type_str": TypeHelper.INTEGER}
    decimal_measures = {"type_str": TypeHelper.BOOLEAN}
    product_name = {"type_str": TypeHelper.TEXT}
    product_description = {"type_str": TypeHelper.TEXT}
    task_id = {"type_str": TypeHelper.INTEGER}

class AnotherORMModel:
    __tablename__ = "this_is_db_table_2"
    ProductID = {
        "type_str": TypeHelper.INTEGER,
        "mapped_column_dict": {"primary_key": True},
    }
    ArtNo = {
        "type_str": TypeHelper.TEXT,
        "mapped_column_dict": {"index": True},
    }
    Name = {"type_str": TypeHelper.TEXT}
    Ratio = {"type_str": TypeHelper.DOUBLE_PRECISION}
    Discount = {"type_str": TypeHelper.DOUBLE_PRECISION}
    Weight = {"type_str": TypeHelper.DOUBLE_PRECISION}
    BriefDescription = {"type_str": TypeHelper.TEXT}
    Description = {"type_str": TypeHelper.TEXT}
    Enabled = {"type_str": TypeHelper.BOOLEAN}
    DateAdded = {
        "type_str": TypeHelper.TIMESTAMP,
        "mapped_column_dict": {"index": True},
    }
    DateModified = {"type_str": TypeHelper.TIMESTAMP}
    Recomended = {"type_str": TypeHelper.BOOLEAN}
    New = {"type_str": TypeHelper.BOOLEAN}
    Bestseller = {"type_str": TypeHelper.BOOLEAN}
    OnSale = {"type_str": TypeHelper.BOOLEAN}
    BrandID = {
        "type_str": TypeHelper.INTEGER,
        "mapped_column_dict": {"index": True},
    }
    AllowPreOrder = {"type_str": TypeHelper.BOOLEAN}
    SortBestseller = {"type_str": TypeHelper.DOUBLE_PRECISION}
    SortNew = {"type_str": TypeHelper.DOUBLE_PRECISION}
    SortDiscount = {"type_str": TypeHelper.DOUBLE_PRECISION}
    UrlPath = {"type_str": TypeHelper.TEXT}
    CategoryEnabled = {"type_str": TypeHelper.BOOLEAN}
    Unit = {"type_str": TypeHelper.TEXT}
    ShippingPrice = {"type_str": TypeHelper.TEXT}
    Hidden = {"type_str": TypeHelper.BOOLEAN}
    ManualRatio = {"type_str": TypeHelper.TEXT}
    main_category = {
        "type_str": TypeHelper.INTEGER,
        "mapped_column_dict": {"index": True},
    }
    is_blocked = {
        "type_str": TypeHelper.BOOLEAN,
        "mapped_column_dict": {"index": True},
    }
    is_art_blocked = {
        "type_str": TypeHelper.BOOLEAN,
        "mapped_column_dict": {"index": True},
    }
