from datetime import datetime

from django.db import transaction
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from products.serializers import ProductListSerializer, ProductSerializer, ProductHistoryUpdateSerializer
from products.models import ProductList, Product, ProductHistory
from accounts.models import Account
from core.decorators import login_required
from core.const import MASTER_ACCOUNT_TYPE

class ProductView(APIView):
    @login_required
    def get(self, request):
        user = request.user

        if Account.objects.get(id = user.id).account_type_id != MASTER_ACCOUNT_TYPE:
            return Response(status.HTTP_401_UNAUTHORIZED)
        
        products = ProductList.objects.filter(is_deleted = False)
        serializer = ProductListSerializer(products, many = True)

        return Response(serializer.data, status.HTTP_200_OK)

    @login_required
    def post(self, request):
        user = request.user

        if Account.objects.get(id = user.id).account_type_id != MASTER_ACCOUNT_TYPE:
            return Response(status.HTTP_401_UNAUTHORIZED)   

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @login_required
    def patch(self, request, product_id):
        user = request.user

        if Account.objects.get(id = user.id).account_type_id != MASTER_ACCOUNT_TYPE:
            return Response(status.HTTP_401_UNAUTHORIZED)
        
        product = get_object_or_404(Product, id = product_id)

        data = request.data
        
        history = ProductHistory.objects.filter(id = product.id).last()
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
        user = request.user

        if Account.objects.get(id = user.id).account_type_id != MASTER_ACCOUNT_TYPE:
            return Response(status.HTTP_401_UNAUTHORIZED)
        
        product = get_object_or_404(Product, id = product_id)

        with transaction.atomic():
            product.is_deleted = True
            product.save()

            now = datetime.now()
            
            history = ProductHistory.objects.filter(id = product_id).last()
            history.id = None
            history.updated_at = now
            history.is_deleted = True
            history.save()

        return Response(status.HTTP_200_OK)