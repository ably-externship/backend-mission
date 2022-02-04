from rest_framework.pagination import PageNumberPagination

class DashboardPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class ListPageNumberPagination(PageNumberPagination):
	page_size = 5


# 상품에 딸린 상품옵션은 페이징이 되면 안되기 때문에, 이렇게 긴 페이지네이션을 따로 생성
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000 #