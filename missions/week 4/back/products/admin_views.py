import json
from datetime import datetime

from django.db import transaction
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from products.serializers import ProductListGetSerializer, ProductSerializer, ProductHistoryUpdateSerializer
from products.models import ProductList, Product, ProductHistory
from core.decorators import login_required
from core.const import MASTER_ACCOUNT_TYPE, SELLER_ACCOUNT_TYPE
from core.utils import image_uploader

class ProductView(APIView):
    @login_required
    def get(self, request):
        account = request.account

        if account.account_type_id != MASTER_ACCOUNT_TYPE and account.account_type_id != SELLER_ACCOUNT_TYPE:
            return Response(status.HTTP_403_FORBIDDEN)

        if account.account_type_id == SELLER_ACCOUNT_TYPE:
            products = ProductList.objects.filter(is_deleted = False, seller_id = account.seller.id)
        else:
            products = ProductList.objects.filter(is_deleted = False)
            
        serializer = ProductListGetSerializer(products, many = True)

        return Response(serializer.data, status.HTTP_200_OK)

    @login_required
    def post(self, request):
        account = request.account

        if account.account_type_id != MASTER_ACCOUNT_TYPE and account.account_type_id != SELLER_ACCOUNT_TYPE:
            return Response(status.HTTP_403_FORBIDDEN)

        data = request.data.dict()
        detail_images = request.FILES.getlist('detail_images')
        main_image = request.FILES.getlist('main_image')
        
        main_image_url = image_uploader(main_image)
        detail_image_url = image_uploader(detail_images)
        
        data = json.loads(data['data'])
        data['main_image_url'] = main_image_url[0]['image_url']
        data['productimage_set'] = detail_image_url
        
        if account.account_type_id == SELLER_ACCOUNT_TYPE:
            data['seller'] = account.seller.id

        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @login_required
    def patch(self, request, product_id):
        account = request.account

        if account.account_type_id != MASTER_ACCOUNT_TYPE and account.account_type_id != SELLER_ACCOUNT_TYPE:
            return Response(status.HTTP_403_FORBIDDEN)
        
        product = get_object_or_404(Product, id = product_id, is_deleted = False)

        if account.account_type_id == SELLER_ACCOUNT_TYPE:
            if product.seller_id != account.seller.id:
                return Response(status.HTTP_403_FORBIDDEN)

        data = request.data
        
        history = ProductHistory.objects.filter(product_id = product.id).last()
        history.id = None
        
        now = datetime.now()
        data['updated_at'] = now
        
        serializer = ProductHistoryUpdateSerializer(instance=history, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_200_OK)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


    @login_required
    def delete(self, request, product_id):
        account = request.account

        if account.account_type_id != MASTER_ACCOUNT_TYPE and account.account_type_id != SELLER_ACCOUNT_TYPE:
            return Response(status.HTTP_403_FORBIDDEN)
        
        product = get_object_or_404(Product, id = product_id, is_deleted = False)

        if account.account_type_id == SELLER_ACCOUNT_TYPE:
            if product.seller_id != account.seller.id:
                return Response(status.HTTP_403_FORBIDDEN)

        with transaction.atomic():
            product.is_deleted = True
            product.save()

            now = datetime.now()
            
            history = ProductHistory.objects.filter(product_id = product.id).last()
            history.id = None
            history.updated_at = now
            history.is_deleted = True
            history.save()

        return Response(status.HTTP_200_OK)