from orm.windows_db.some_schema import AnotherORMModel, SomeTable

mx_router = {
    "VendorProduct": AnotherORMModel,
    "ProductsData": SomeTable,
}

windows_router = dict(mx_router)
