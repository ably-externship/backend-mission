import pymysql
from missions.week_1.back.db import Singleton
from missions.week_1.back.mbly.settings import DATABASES, ENV


class SqlDb(metaclass=Singleton):
    def __init__(self, db_name):
        self._host = DATABASES[ENV]['HOST']
        self._user = DATABASES[ENV]['USER']
        self._password = DATABASES[ENV]['PASSWORD']
        self._port = DATABASES[ENV]['PORT']
        self._db = pymysql.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            db=db_name,
            port=self._port
        )
        self._cursor = self._db.cursor(pymysql.cursors.DictCursor)

    def init(self):
        self._host = None,
        self._user = None,
        self._password = None,
        self._db = None
        self._port = None

    def execute(self, query, args={}):
        self._cursor.execute(query, args)

    def execute_one(self, query, args={}):
        self._cursor.execute(query, args)
        row = self._cursor.fetchone()
        return row

    def execute_all(self, query, args={}):
        if args:
            self._cursor.execute(query, args)
        else:
            self._cursor.execute(query)
        row = self._cursor.fetchall()
        return row

    def commit(self):
        self._db.commit()

    def set_sql_instance(self, ENV):
        self._host = DATABASES[ENV]['HOST']
        self._user = DATABASES[ENV]['USER']
        self._password = DATABASES[ENV]['PASSWORD']
        self._port = DATABASES[ENV]['PORT']

