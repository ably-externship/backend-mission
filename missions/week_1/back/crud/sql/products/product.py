from missions.week_1.back.crud.sql.products import ProductBaseCrud


class ProductsCrud(ProductBaseCrud):
    db_name = 'products'
    table_name = 'product'