class ProductQuery:
    keyword: 1 = None
    page: int = 1
    display_cnt: int = 10
    where: str = 'name'
    order_by: str = 'stars'
    sort: str = 'DESC'
