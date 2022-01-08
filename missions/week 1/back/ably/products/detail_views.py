from django.http import JsonResponse
from django.views import View

from products.models import Product, ProductOption

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects\
                .select_related('seller')\
                .prefetch_related('producthistory_set', 'productoption_set', 'productimage_set')\
                .get(id = product_id)

            product_detail = product.producthistory_set.last()
            
            if not product_detail.is_displayed or product_detail.is_deleted:
                return JsonResponse({'message' : 'Not Found'}, status = 404)
            
            product_options = ProductOption.objects\
                .select_related('color', 'size')\
                .filter(product_id = product_id)
            
            product_info = {
                'id' : product.id,
                'name' : product_detail.name,
                'price' : product_detail.price,
                'discount_price' : product_detail.discount_price,
                'is_sold_out' : product_detail.is_sold_out,
                'images' : [
                    image.image_url for image in product.productimage_set.all()
                ],
                'options' : [
                    {
                        'color' : option.color.color,
                        'size' : option.size.size,
                        'stock' : option.stock,
                        'is_sold_out' : option.is_sold_out,
                        'extra_price' : option.extra_price
                    }
                    for option in product_options
                ]
            }

            seller_info = {
                'id' : product.seller.id,
                'name' : product.seller.name,
                'image_url' : product.seller.image_url
            }

            return JsonResponse({'product' : product_info, 'seller' : seller_info}, status = 200)

        except Product.DoesNotExist:
            return JsonResponse({'message' : 'Not Found'}, status = 404)