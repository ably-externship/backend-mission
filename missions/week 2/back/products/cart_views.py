import json

from django.http import JsonResponse
from django.views import View

from core.decorators import login_required
from products.models import Cart

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

class CartView(View):
    @login_required
    def post(self, request):
        user = request.user
        data = json.loads(request.body)

        filter_set = {
            'user_id' : user.id,
            'product_id' : data['product_id'],
            'product_option_id' : data['product_option_id']
        }

        if Cart.objects.filter(**filter_set).exists():
            cart = Cart.objects.get(**filter_set)
            cart.quantity += data.quantity
        
        else:
            Cart.objects.creat(**filter_set, quantity = data.quantity)

        return JsonResponse({'message' : 'Success'}, status = 201)

    @login_required
    def patch(self, request):
        user = request.user
        data = json.loads(request.body)

        Cart.objects.filter(
            user_id = user.id, 
            product_id = data['product_id'], 
            product_option_id = data['product_option_id']
        ).update(
            product_option_id = data['product_option_id'], 
            quantity=data['quantity']
            )

        return JsonResponse({'message' : 'Success'}, status = 200)

    @login_required
    def delete(self, request):
        user = request.user
        data = json.loads(request.body)
        products = data['products']

        for product in products:
            Cart.objets.get(
                product_id = product['product_id'], 
                product_option_id = product['product_option_id']
                ).delete()

        return JsonResponse({'message' : 'Success'}, status = 200)