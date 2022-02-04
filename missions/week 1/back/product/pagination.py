from rest_framework.pagination import PageNumberPagination

class DashboardPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class ListPageNumberPagination(PageNumberPagination):
	page_size = 5