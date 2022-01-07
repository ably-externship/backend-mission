from datetime import datetime


class BaseCrud:
    db_name = ''
    table_name = ''

    @classmethod
    def get_find_sql_query(
            cls,
            column='*',
            condition=None,
            order_by=None,
            skip=0,
            sort='DESC',
            limit=9999
    ):
        sql = f'SELECT {column} '
        sql += f'FROM {cls.table_name} '

        if condition:
            sql += f'WHERE {condition} '
        if order_by:
            sql += f'ORDER BY {order_by} {sort} '
        sql += f'LIMIT {skip}, {limit}'

        return sql + ';'

