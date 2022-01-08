from missions.week_1.back.crud.sql.meta import MetaBaseCrud
from missions.week_1.back.db.sql import SqlDb


class UserCrud(MetaBaseCrud):
    db_name = 'meta'
    table_name = 'user'

    @classmethod
    def create_user(cls, register_form):
        sql = cls.get_insert_sql_query(register_form)
        db = SqlDb(cls.db_name)
        values = register_form.values()
        values = tuple(values)
        try:
            db.execute(sql, values)
            db.commit()
        except BaseException as e:
            print(e.args)
