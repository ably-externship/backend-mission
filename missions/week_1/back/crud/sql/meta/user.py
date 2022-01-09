from missions.week_1.back.crud.sql.meta import MetaBaseCrud
from missions.week_1.back.db.sql import SqlDb


class UserCrud(MetaBaseCrud):
    db_name = 'meta'
    table_name = 'user'

    @classmethod
    def get_user(cls, user_id):
        sql = cls.get_find_sql_query(
            where='user_id',
            like=user_id
        )
        db = SqlDb(cls.db_name)
        user = db.execute_all(sql)

        if user:
            return user
        return {}

    @classmethod
    def create_user(cls, register_form):
        sql_query = cls.get_insert_sql_query(register_form)
        db = SqlDb(cls.db_name)
        values = register_form.values()
        try:
            db.execute(sql_query, tuple(values))
            db.commit()
            return True, None
        except BaseException as e:
            print(e.args)
            error_message = e.args
            return False, error_message
