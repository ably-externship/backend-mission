from missions.week_1.back.crud.sql.help import HelpBaseCrud
from missions.week_1.back.db.sql import SqlDb


class HelpCrud(HelpBaseCrud):
    db_name = 'help'
    table_name = 'help'

    @classmethod
    def get_help_list(
            cls,
            page: int = 1,
            limit: int = 10,
            help_type: str = None
    ):
        skip = (page - 1) * limit
        sql_query = cls.get_find_sql_query(
            skip=skip,
            like=help_type,
            limit=limit
        )

        db = SqlDb(cls.db_name)
        result = db.execute_all(sql_query)

        return result

    @classmethod
    def create_help(cls, help_form: dict):
        sql_query = cls.get_insert_sql_query(help_form)
        db = SqlDb(cls.db_name)
        values = help_form.values()
        try:
            db.execute(sql_query, tuple(values))
            db.commit()
            return True, None
        except BaseException as e:
            print(e.args)
            error_message = e.args
            return False, error_message
