from missions.week_1.back.crud.sql.products import ProductBaseCrud
from missions.week_1.back.db.sql import SqlDb


class ProductCrud(ProductBaseCrud):
    db_name = 'products'
    table_name = 'product'

    @classmethod
    def get_products(cls, page=1, display_cnt=9999, order_by='id', sort_order='DESC'):
        skip = (page - 1) * display_cnt
        sql_query = cls.get_find_sql_query(
            order_by='id',
            skip=skip,
            sort=sort_order,
            limit=5
        )
        db = SqlDb(cls.db_name)
        result = db.executeAll(sql_query)

        return result


