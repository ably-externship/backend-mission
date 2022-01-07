from datetime import datetime


class BaseCrud:
    db_name = ''
    table_name = ''

    @classmethod
    def get_find_sql_query(
            cls,
            select='*',
            where=None,
            like=None,
            order_by=None,
            skip=0,
            sort='DESC',
            limit=9999
    ):
        sql = f'SELECT {select} '
        sql += f'FROM {cls.table_name} '

        if where:
            sql += f'WHERE {where} '
        if like:
            sql += f'LIKE {like} '
        if order_by:
            sql += f'ORDER BY {order_by} {sort} '
        sql += f'LIMIT {skip}, {limit}'

        return sql + ';'

