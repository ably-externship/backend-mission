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

        return sql

    @classmethod
    def get_insert_sql_query(cls, obj):
        sql = f'INSERT '
        sql += f'INTO {cls.table_name}'

        table_field = '('
        value_format = 'VALUES('
        for idx, key in enumerate(obj):
            table_field += f'{key}, ' if len(obj) - 1 != idx else f'{key}) '
            value_format += '%s, ' if len(obj) - 1 != idx else '%s)'

        sql += table_field
        sql += value_format

        return sql

