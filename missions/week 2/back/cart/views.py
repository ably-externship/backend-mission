from django.shortcuts import render
from .models import Cart
from product.models import Product
from user.models import Account

def cart(request):

    conn_user = request.user
    cart_id = Account.objects.get(username=conn_user).id  # cart_id, user_id
    print('1111',cart_id)
    print('2222',Product.cart.through.objects.all())
    carts=Cart.product.through.objects.filter(cart_id=cart_id)
    temp=Product.objects.all()
    # print('~~~',temp.cart.all())
    print('3333',carts.product_set.all())
    # Cart 데이터의 product_id 저장하기
    products=[]
    product_id=[]
    for cart in carts.values():
        print(cart)
        product_id.append(cart['product_id'])
        # temp=Product.objects.filter(id=cart['product_id'])
        # products.append(temp)

    # products=Product.objects.filter(id=)
    print('4444',product_id)

    products={}



    # products=Product.objects.filter(id=product_id)
    #
    #
    # print('4444',products)

    # print('1111',products)

    return render(request, 'cart.html')

# def cart_id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart
#
#
# def add_cart(request,product_id):
#     product = Product.objects.get(id=product_id)
#     try:
#         cart = Cart.objects.get(product=product_id)
#     except Cart.DoesNotExist:
#         cart = Ca