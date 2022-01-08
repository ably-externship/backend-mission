from missions.week_1.back.crud.sql.products import ProductBaseCrud
from missions.week_1.back.db.sql import SqlDb
from missions.week_1.back.api.product.models import ProductQuery


class ProductCrud(ProductBaseCrud):
    db_name = 'products'
    table_name = 'product'

    @classmethod
    def get_products(
            cls,
            page: int = 1,
            display_cnt: int = 10,
            order_by: str = 'stars',
            sort_order: str = 'DESC'
    ):
        skip = (page - 1) * display_cnt
        sql_query = cls.get_find_sql_query(
            order_by=order_by,
            skip=skip,
            sort=sort_order,
            limit=5
        )
        db = SqlDb(cls.db_name)
        result = db.execute_all(sql_query)

        return result

    @classmethod
    def search_products(cls, product_query: ProductQuery):
        skip = (product_query.page - 1) * product_query.display_cnt
        sql_query = cls.get_find_sql_query(
            select='name',
            where=product_query.where,
            like=f'%{product_query.keyword}%',
            order_by=product_query.order_by,
            skip=skip,
            sort=product_query.sort,
            limit=5
        )
        db = SqlDb(cls.db_name)
        result = db.execute_all(sql_query)

        return result

