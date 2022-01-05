import pymysql
from missions.week_1.back.db import Singleton


class SqlDb(metaclass=Singleton):
    def __init__(self):
        self._server = '127.0.0.1',
        self._user = 'fbaudrl96',
        self._password = 'audrl30734',
        self._db = None,
        self._port = '3306'

    def init(self):
        self._server = None,
        self._user = None,
        self._password = None,
        self._db = None,
        self._port = None

    def connect(self, db):
        return pymysql.connect(
            host=self._server,
            user=self._user,
            password=self._password,
            db=db,
            port=self._port
        )