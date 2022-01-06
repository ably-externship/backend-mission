from missions.week_1.back.crud.sql.meta import MetaBaseCrud


class EmployeeCrud(MetaBaseCrud):
    db_name = 'meta'
    table_name = 'employee'