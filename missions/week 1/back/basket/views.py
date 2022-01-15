from django.shortcuts import render, redirect

# # Create your views here.
# @csrf_exempt #ViewSet
# def basket_list(request, pk):
#     #request 에서 사용자 가져와
#     #request 에서 상품품    if request.method == 'GET':
#         questions = Question.objects.filter(shop=pk)
#         #serializer = QuestionSerializer(questions, many=True)
#         return render(request, 'qna_list.html', {'questions': questions})

# @csrf_exempt #ViewSet
# def basket_update(request, pk):
#     #count, size, color
#     #request 에서 사용자 가져와
#     #request 에서 상품품    if request.method == 'GET':
#         questions = Question.objects.filter(shop=pk)
#         #serializer = QuestionSerializer(questions, many=True)
#         return render(request, 'qna_list.html', {'questions': questions})
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from lionuser.models import Lionuser
from product.models import Product, ProductOptionGroup, ProductOptionGroupItem
from .models import Basket
from .seiralizer import BasketSerializer
from django.http import HttpResponse, JsonResponse

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
@csrf_exempt
def basket_list(request):
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        print("User is not logged in :(")
    user = Lionuser.objects.get(username=request.user.username)

    print(request.user.username)
    print(user)
    print(user.id)
    user_id = user.id
    result = Basket.objects.filter(user=user.id)
    #
    print(result)
    for r in result:
        print(r.product)
        print(r.option_2_type)
    # serializer = BasketSerializer(result, many=True)
    # print(serializer)
    return render(request, 'mypage.html',{'user':request.user.username,'userId':user_id ,'basket':result})

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
@csrf_exempt
def basket_create(request, item):

    #user
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
    else:
        print("User is not logged in :(")
    user = Lionuser.objects.get(username=request.user.username)

    #item
    if request.method == 'POST':
        count = request.POST.get('data')
        size = request.POST.get('size')
        color = request.POST.get('color')

        pd = Product.objects.get(pk=item)

        optionGroups = ProductOptionGroup.objects.filter(product=item)

        i = 1
        for optionGroup in optionGroups:
            print(optionGroup.id)
            print(optionGroup.optionGroup.strip())
            print(request.POST.get(f'{optionGroup.optionGroup.strip()}'))
            if optionGroup.optionGroup == 'size':
                size = optionGroup.id
            else:
                color = optionGroup.id

        sizeOption = ProductOptionGroupItem.objects.get(productOptionGroup=size, optionItem= request.POST.get('size'))#.id
        colorOption = ProductOptionGroupItem.objects.get(productOptionGroup=color, optionItem=request.POST.get('color'))


        Basket.objects.create(count=count, user=user, product=pd, option_1_name=sizeOption.optionItem,option_2_name=colorOption.optionItem )
        print("장바구니 추가")

        return redirect(reverse('mypage'))

@csrf_exempt
def basket_delete_v2(request, user):

    if request.method == 'GET':
        return "ㅅㅄㅄ"
    print(request)
    # item
    if request.method == 'POST':
        basket = request.POST.get('basket')
        print(basket)
        basket_to = Basket.objects.get(pk=basket)

        print(basket_to)
        basket_to.delete()

        return JsonResponse({'status': 200, 'message': '장바구니 삭제'})


#
@csrf_exempt
def basket_update(request, user):
    #item
    if request.method == 'POST':
        basket = request.POST.get('basket')
        count_to = request.POST.get('count')
        print(count_to)
        print(basket)
        print('asdfasdfasdfasdfsdaasd---------')

        basket_to = Basket.objects.get(pk=basket)
        print(basket_to)

        basket_to.count = int(count_to)
        print(basket_to)
        basket_to.save()
        return JsonResponse({'status': 200, 'message': '장바구니 수정'})

