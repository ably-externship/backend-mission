from datetime import datetime
from missions.week_1.back.db.sql import SqlDb


class BaseCrud:
    db_name = ''
    table_name = ''

    @classmethod
    def get_database(cls):
        db = SqlDb.get_database(cls.db_name)
        cursor = db.cursor()
        return cursor

    @classmethod
    def get_find_sql(cls, column='*', condition=None, order_by=None, limit=99999):
        sql = f'SELECT {column}' \
              f'FROM {cls.table_name}'

        if condition:
            sql += f'WHERE {condition}'
        if order_by:
            sql += f'ORDER BY {order_by}'
        if limit:
            sql += f'LIMIT {limit}'

        return sql

    @classmethod
    def find(cls, db, sql):
        result = db.excute(sql)
        return result

    @classmethod
    def insert(cls, db, sql):
        pass


