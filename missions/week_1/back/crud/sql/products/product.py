from missions.week_1.back.crud.sql.products import ProductBaseCrud
from missions.week_1.back.db.sql import SqlDb
# from missions.week_1.back.api.product.models import ProductQuery


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
    def search_products(cls, query):
        page = query.get('page') or 1
        limit = query.get('limit') or 5
        skip = (page - 1) * limit
        keyword = query.get('keyword') or None
        order_by = query.get('order_by') or 'stars'
        sort = query.get('sort') or 'DESC'
        where = query.get('where') or 'name'
        select = query.get('select') or '*'

        sql_query = cls.get_find_sql_query(
            select=select,
            where=where,
            like=keyword,
            order_by=order_by,
            skip=skip,
            sort=sort,
            limit=5
        )
        db = SqlDb(cls.db_name)
        result = db.execute_all(sql_query)

        return result

