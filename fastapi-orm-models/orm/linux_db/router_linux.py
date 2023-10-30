from orm.linux_db.schema_one import CategoriesDimensions
from orm.linux_db.schema_two import Categories

first_schema_router = {"CategoriesDimensions": CategoriesDimensions}
second_chema_router = {"Categories": Categories}

linux_db_router = dict(first_schema_router, **second_chema_router)
