import json

from django.http import JsonResponse
from django.views import View

from core.decorators import login_required
from products.models import CartItem, CartItemList

"""
post/patch - request.body
{
    "product_id" : 3,
    "product_option_id" : 9,
    "quantity" : 1
}

delete - request.body
{
    "products" : [
        {
            "product_id" : 1,
            "product_option_id" : 5
        },
        {
            "product_id" : 2,
            "product_option_id" : 7
        }
    ]
}
"""

class CartItemView(View):
    @login_required
    def post(self, request):

        user = request.user
        data = json.loads(request.body)

        filter_set = {
            'user_id' : user.id,
            'product_id' : data['product_id'],
            'product_option_id' : data['product_option_id']
        }
        
        if CartItem.objects.filter(**filter_set).exists():
            cart = CartItem.objects.get(**filter_set)
            cart.quantity += data['quantity']
            cart.save()
        
        else:
            CartItem.objects.create(**filter_set, quantity = data['quantity'])

        return JsonResponse({'message' : 'Success'}, status = 201)

    @login_required
    def get(self, request):
        user = request.user
        products = CartItemList.objects.filter(user_id = user.id)

        cart_items = [
            {
                'product_id' : product.product_id,
                'product_name' : product.product_name,
                'main_image_url' : product.main_image_url,
                'product_option_id' : product.product_option_id,
                'color' : product.color,
                'size' : product.size,
                'price' : product.price,
                'discount_price' : product.discount_price,
                'extra_price' : product.extra_price,
                'quantity' : product.quantity,
                'is_sold_out' : product.is_sold_out
            }
            for product in products
        ]

        return JsonResponse({'cart_items' : cart_items}, status = 200)

    @login_required
    def patch(self, request):
        user = request.user
        data = json.loads(request.body)
        
        CartItem.objects.filter(
            user_id = user.id, 
            product_id = data['product_id'], 
            product_option_id = data['product_option_id']
        ).update(
            quantity=data['quantity']
            )

        return JsonResponse({'message' : 'Success'}, status = 200)

    @login_required
    def delete(self, request):
        user = request.user
        data = json.loads(request.body)
        products = data['products']

        for product in products:
            CartItem.objects.get(
                user_id = user.id,
                product_id = product['product_id'], 
                product_option_id = product['product_option_id']
                ).delete()

        return JsonResponse({'message' : 'Success'}, status = 200)