from django.http import JsonResponse
from django.views import View

from products.models import ProductCategory, Color, Size
from accounts.models import Seller

class CategoryView(View):
    def get(self, request):
        categories = ProductCategory.objects.prefetch_related('productsubcategory_set').all()

        result = [
            {
                'id' : category.id,
                'name' : category.name,
                'subcategories' : [
                    {
                        'id' : subcategory.id,
                        'name' : subcategory.name
                        } for subcategory in category.productsubcategory_set.all()
                    ]
                } for category in categories
            ]

        return JsonResponse({'result' : result}, status=200)

class ColorView(View):
    def get(self, request):
        colors = Color.objects.all()

        result = [
            {
                'id' : color.id,
                'name' : color.color
            } for color in colors
        ]

        return JsonResponse({'result' : result}, status=200)

class SizeView(View):
    def get(self, request):
        sizes = Size.objects.all()

        result = [
            {
                'id' : size.id,
                'name' : size.size
            } for size in sizes
        ]

        return JsonResponse({'result' : result}, status=200)

class SellerView(View):
    def get(self, request):
        sellers = Seller.objects.all()

        result = [
            {
                'id' : seller.id,
                'name' : seller.name
            } for seller in sellers
        ]

        return JsonResponse({'result' : result}, status=200)