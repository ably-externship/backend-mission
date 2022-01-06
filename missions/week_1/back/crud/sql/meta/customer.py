from missions.week_1.back.crud.sql.meta import MetaBaseCrud


class CustomerCrud(MetaBaseCrud):
    db_name = 'meta'
    table_name = 'customer'