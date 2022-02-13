from django.http import JsonResponse
from django.views import View
from django.db.models import Case, When
from elasticsearch import Elasticsearch

from products.models import ProductList
from my_settings import ELASTICSEARCH_URL, ELASTICSEARCH_USER, ELASTICSEARCH_PASSWORD

class ProductListView(View):
    def get(self, request):
        PAGINATION_LIMIT = 8
        
        search_word = request.GET.get('search_word', '')
        page = int(request.GET.get('page', 1))
        offset = (page - 1) * PAGINATION_LIMIT
        limit = offset + PAGINATION_LIMIT

        if search_word:
            elasticsearch = Elasticsearch(ELASTICSEARCH_URL, http_auth=(ELASTICSEARCH_USER, ELASTICSEARCH_PASSWORD))

            query = f"""
            SELECT product_id
                FROM products
            WHERE 
                MATCH(product_name, '{search_word}')
                OR MATCH(seller_name, '{search_word}')
                OR MATCH(category_name, '{search_word}')
                OR MATCH(subcategory_name, '{search_word}')
            ORDER BY score() DESC
            """

            response = elasticsearch.sql.query(body={"query":query})

            product_ids = [row[0] for row in response['rows']]

            order = Case(*[When(id=id, then=pos) for pos, id in enumerate(product_ids)])

            products = ProductList.objects.filter(
                product_id__in = product_ids,
                is_deleted = False,
                is_displayed = True).order_by(order)

        else:
            products = ProductList.objects.filter(
                is_deleted = False,
                is_displayed = True)

        product_lists = [
            {
                'id' : product.product_id,
                'product_name' : product.product_name,
                'price' : product.price,
                'discount_price' : product.discount_price,
                'main_image_url' : product.main_image_url,
                'seller_name' : product.seller_name
            }
            for product in products[offset:limit]
        ]
        
        return JsonResponse(
            {
                'product_lists' : product_lists, 
                'product_counts' : products.count()
                }, 
            status = 200)
