from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Shop
from .serializers import ShopSerializer
from product.models import Product, ProductOptionGroup, ProductOptionGroupItem, ProductImg
from product.serializers import ProductSerializer, ProductOptionGroupSerializer,ProductOptionGroupItemSerializer
from board.models import Question
from board.serializers import QuestionSerializer
import json

def index(request):
    if request.method == 'GET':
        print("test jenkins")
        print("test jenkins")
        print("test jenkins")
        return "jenkins"

        shop = Shop.objects.all()
        #serializer = ShopSerializer(shop, many=True)
        return render(request, 'index.html', {'shop_list': shop})  # 쇼핑몰 -> item -> item 상세 페이지 or jQuery를 통해


class ShopViewSet(viewsets.ViewSet):
    def create(self, request):  # /api/shop
        serializer = ShopSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@csrf_exempt
def shop_item(request, shop):
    if request.method == 'GET':
        products = Product.objects.filter(shop=shop)
        for product in products:
            product = Product.objects.get(id=product.id)
            optionGroups = ProductOptionGroup.objects.filter(product=product.id)

            stock = 0 #재고, option Item 을 group 마다 재고 확인해야
            i = 0
            for optionGroup in optionGroups:
                i += 1;
                optionItems = ProductOptionGroupItem.objects.filter(productOptionGroup=optionGroup.id)
                for item in optionItems: #재고 확인
                    stock += item.stock
            product.calculateStock(stock / i) #전체 재고 확인
        return render(request, 'product.html', {'product_list': products, 'shop':shop})
        #serializer = ProductSerializer(products, many=True)
        #return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        shop_item = Shop.objects.get(id=shop)
        form_data = json.loads(request.body.decode())
        product_name = form_data['product_name']
        description = form_data['description']
        price = form_data['price']
        stock = form_data['stock']
        shop_item.product_set.create(shop=int(shop), product_name=product_name, description=description, price=price, stock=stock)

        product = Product.objects.get(pk=shop_item.product_set.latest('id').id)
        optionGroupList = form_data['option_group']
        for optionGroup1 in optionGroupList:
            optionGroup = optionGroup1['optionGroup']
            product.productoptiongroup_set.create(product=product.id, optionGroup=optionGroup)
            optionGroup_item = ProductOptionGroup.objects.get(pk=product.productoptiongroup_set.latest('id').id)
            optionGroupItem = optionGroup1["optionItem"]

            for option in optionGroupItem:

                optionItem = option['optionItem']

                addPrice = option['addPrice']
                optionGroup_item.productoptiongroupitem_set.create(productOptionGroup=optionGroup_item.id, optionItem=optionItem, addPrice = addPrice)

        return HttpResponse("hi")


@csrf_exempt
def shop_item_detail(request, shop, item):
    if request.method == 'GET':
        product = Product.objects.get(id=item)
        # productSerializer = ProductSerializer(product)
        optionGroups = ProductOptionGroup.objects.filter(product=item)
        # optionGroupSerializer = ProductOptionGroupSerializer(optionGroups, many=True)

        choices = []
        for optionGroup in optionGroups: #주문시 option마다 추가가격 확인
            optionItems = ProductOptionGroupItem.objects.filter(productOptionGroup=optionGroup.id)
            # optionItemSerializer = ProductOptionGroupItemSerializer(optionItems, many=True)
            choices.append(optionItems)

        #img
        imgs = ProductImg.objects.filter(product=item)
        return render(request, 'product_detail.html', {'product': product, 'optionGroups': optionGroups, 'optionItems': choices, 'imgs': imgs, 'itemId':item})




# from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# @api_view(['GET'])
# @permission_classes((IsAuthenticated, ))
# @authentication_classes((JSONWebTokenAuthentication,))


@csrf_exempt #ViewSet
def qna_list(request, pk):
    if request.method == 'GET':
        questions = Question.objects.filter(shop=pk)
        #serializer = QuestionSerializer(questions, many=True)
        return render(request, 'qna_list.html', {'questions': questions})

@csrf_exempt
def shop_qna_create(request, shop):
    if request.method == 'POST':
        shop = Shop.objects.get(id=shop)
        #product = Product.objects.get(id=21) #질문 임의로 선택할 수 있어야 함 default

        title = request.POST.get('title_give')
        user = request.POST.get('user_give')
        qna = request.POST.get('qna_give')

        qna = shop.question_set.create(shop=shop, title=title, description=qna) #, product = product)
        serializer = QuestionSerializer(qna)
        # return Response(serializer.data)
        return JsonResponse({'msg': 'suc'}, status=201)

    elif request.method == 'GET':
        return render(request,'qna.html')

