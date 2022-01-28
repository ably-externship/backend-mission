from django.http import JsonResponse
from django.views import View

from products.models import ProductList

class ProductListView(View):
    def get(self, request):
        PAGINATION_LIMIT = 9
        
        search_word = request.GET.get('search_word', '')
        page = int(request.GET.get('page', 1))
        offset = (page - 1) * PAGINATION_LIMIT
        limit = offset + PAGINATION_LIMIT

        products = ProductList.objects.filter(
            product_name__icontains = search_word,
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
