from accounts.models import User, Seller
from .models import BaseMerchandise, Merchandise
from .serializers import (
    SellerMerchandiseNestedListSerializer,
    SellerBaseMerchandiseCreateSerializer,
    SellerMerchandiseCreateSerializer,
    SellerBaseMerchandiseUpdateSerializer,
    SellerMerchandiseUpdateSerializer
)
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from uuid import uuid4
import os
import ast
import boto3


class SellerBaseMerchandiseListView(ListAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = BaseMerchandise.objects.all()
    serializer_class = SellerMerchandiseNestedListSerializer
    
    @csrf_exempt
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('Authorization',
            openapi.IN_HEADER,
            description="Bearer access_token",
            type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request, *args, **kwargs):
        '''
            empty
            
            ---
        '''
        
        user, token = JWTAuthentication().authenticate(request)
        
        try:
            seller_obejct = User.objects.prefetch_related('seller').get(id=str(user)).seller
            self.queryset = BaseMerchandise.objects.filter(seller=seller_obejct)
            merchandise_data = self.list(request, *args, **kwargs).data
            
            response = {}
            response['message'] = 'SUCCESSFULLY GET MERCHANDISES'
            response['count'] = len(merchandise_data)
            response['merchandises'] = merchandise_data
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=200)
        except:
            response = {}
            response['message'] = 'NOT FOUND MERCHANDISES'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=404)


class SuperuserMerchandiseListView(ListAPIView):
    
    permission_classes = [IsAuthenticated]
    queryset = BaseMerchandise.objects.all()
    serializer_class = SellerMerchandiseNestedListSerializer
    
    @csrf_exempt
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('Authorization',
            openapi.IN_HEADER,
            description="Bearer access_token",
            type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request, *args, **kwargs):
        '''
            empty
            
            ---
        '''
        
        user, token = JWTAuthentication().authenticate(request)
        if User.objects.get(id=str(user)).is_superuser is False:
            return JsonResponse({'error': 'SUPERUSER AUTHENTICATION ERROR'}, status=403)
        
        try:
            merchandise_data = self.list(request, *args, **kwargs).data
            
            response = {}
            response['message'] = 'SUCCESSFULLY GET MERCHANDISES'
            response['count'] = len(merchandise_data)
            response['merchandises'] = merchandise_data
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=200)
        except:
            response = {}
            response['message'] = 'NOT FOUND MERCHANDISES'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=404)


class SuperuserMerchandiseCreateView(CreateAPIView):
    
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = SellerBaseMerchandiseCreateSerializer
    
    def perform_create(self, serializer):
        return serializer.save()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            raise ValidationError('serializer validation error')
        
        return self.perform_create(serializer)
    
    @csrf_exempt
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer access_token", type=openapi.TYPE_STRING)])
    def post(self, request, *args, **kwargs):
        '''
            empty
            
            ---
        '''
        
        user, token = JWTAuthentication().authenticate(request)
        if User.objects.get(id=str(user)).is_superuser is False:
            return JsonResponse({'error': 'SUPERUSER AUTHENTICATION ERROR'}, status=403)
        
        try:
            files = {}
            main_img = request.FILES.get('main_img')
            if main_img:
                files['main_img'] = main_img
            sub_img_0 = request.FILES.get('sub_img_0')
            if sub_img_0:
                files['sub_img_0'] = sub_img_0
            sub_img_1 = request.FILES.get('sub_img_1')
            if sub_img_1:
                files['sub_img_1'] = sub_img_1
            sub_img_2 = request.FILES.get('sub_img_2')
            if sub_img_2:
                files['sub_img_2'] = sub_img_2
            merchandises = ast.literal_eval(request.data['merchandises'])
        except KeyError:
            return JsonResponse({'error': 'REQUEST DATA KEY ERROR'}, status=400)
        
        try:
            s3_client = boto3.client('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
            common_code = uuid4().hex[:8]
            request.data['common_code'] = common_code
            for i, key in enumerate(files.keys()):
                s3_path = f'{common_code}/No0{i+1}/{files[key]}'
                s3_client.upload_fileobj(files[key], os.environ.get('AWS_BUCKET_NAME'), s3_path, ExtraArgs = {"ContentType": 'image/jpeg'})
                s3_url = os.environ.get('AWS_S3_ADDRESS') + s3_path
                request.data[key] = s3_url
        except:
            response = {}
            response['message'] = 'AWS IMAGEFILE UPLOAD FAIL'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=400)
        
        try:
            basemerchandise_object = self.create(request, *args, **kwargs)
            request.data['basemerchandise'] = basemerchandise_object.id
            self.serializer_class = SellerMerchandiseCreateSerializer
            for i, merchandise in enumerate(merchandises):
                if len(str(i+1)) == 1:
                    option_code = 'No0'+str(i+1)
                else:
                    option_code = 'No'+str(i+1)
                request.data['full_code'] = common_code + option_code
                request.data['color'] = merchandise['color']
                request.data['size'] = merchandise['size']
                request.data['current_stock'] = merchandise['current_stock']
                request.data['safety_stock'] = merchandise['safety_stock']
                request.data['soldout_state'] = merchandise['soldout_state']
                request.data['on_sale'] = merchandise['on_sale']
                request.data['on_display'] = merchandise['on_display']
                self.create(request, *args, **kwargs)
            response = {}
            response['message'] = 'SUCCESSFULLY CREATE MERCHANDISES'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=201)
        except:
            response = {}
            response['message'] = 'NOT FOUND MERCHANDISES'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=400)


class SuperuserOptionMerchandiseCreateView(CreateAPIView):
    
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = SellerMerchandiseCreateSerializer
    
    def perform_create(self, serializer):
        return serializer.save()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            raise ValidationError('serializer validation error')
        
        return self.perform_create(serializer)
    
    @csrf_exempt
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer access_token", type=openapi.TYPE_STRING)])
    def post(self, request, *args, **kwargs):
        '''
            empty
            
            ---
        '''
        
        user, token = JWTAuthentication().authenticate(request)
        if User.objects.get(id=str(user)).is_superuser is False:
            return JsonResponse({'error': 'SUPERUSER AUTHENTICATION ERROR'}, status=403)
        
        try:
            merchandises = request.data['merchandises']
            common_code = request.data['common_code']
        except KeyError:
            return JsonResponse({'error': 'REQUEST DATA KEY ERROR'}, status=400)
        
        try:
            cnt = len(Merchandise.objects.filter(full_code__contains=common_code))
            for i, merchandise in enumerate(merchandises):
                if len(str(cnt+i+1)) == 1:
                    option_code = 'No0'+str(cnt+i+1)
                else:
                    option_code = 'No'+str(cnt+i+1)
                request.data['full_code'] = common_code + option_code
                request.data['color'] = merchandise['color']
                request.data['size'] = merchandise['size']
                request.data['current_stock'] = merchandise['current_stock']
                request.data['safety_stock'] = merchandise['safety_stock']
                request.data['soldout_state'] = merchandise['soldout_state']
                request.data['on_sale'] = merchandise['on_sale']
                request.data['on_display'] = merchandise['on_display']
                self.create(request, *args, **kwargs)
            response = {}
            response['message'] = 'SUCCESSFULLY CREATE MERCHANDISES'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=201)
        except:
            response = {}
            response['message'] = 'CREATE FAIL'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=400)


class SuperuserBaseMerchandiseUpdateDeleteView(UpdateAPIView, DestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    lookup_field = 'pk'
    queryset = BaseMerchandise.objects.all()
    serializer_class = SellerBaseMerchandiseUpdateSerializer
    
    @csrf_exempt
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer access_token", type=openapi.TYPE_STRING)])
    def patch(self, request, *args, **kwargs):
        '''
            empty
            
            ---
        '''
        
        user, token = JWTAuthentication().authenticate(request)
        if User.objects.get(id=str(user)).is_superuser is False:
            return JsonResponse({'error': 'SUPERUSER AUTHENTICATION ERROR'}, status=403)
        
        try:
            files = {
                'main_img': None,
                'sub_img_0': None,
                'sub_img_1': None,
                'sub_img_2': None
            }
            if 'main_img' in request.data.keys():
                files['main_img'] = request.FILES.get('main_img')
            if 'sub_img_0' in request.data.keys():
                files['sub_img_0'] = request.FILES.get('sub_img_0')
            if 'sub_img_1' in request.data.keys():
                files['sub_img_1'] = request.FILES.get('sub_img_1')
            if 'sub_img_2' in request.data.keys():
                files['sub_img_2'] = request.FILES.get('sub_img_2')
        except KeyError:
            return JsonResponse({'error': 'REQUEST DATA KEY ERROR'}, status=400)
        
        try:
            s3_client = boto3.client('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
            s3_address = os.environ.get('AWS_S3_ADDRESS')
            basemerchandise_object = self.get_object()
            common_code = basemerchandise_object.common_code
            if files['main_img'] and basemerchandise_object.main_img:
                s3_client.delete_object(Bucket=os.environ.get('AWS_BUCKET_NAME'), Key=f'{(basemerchandise_object.main_img).split(s3_address)[1]}')
            if files['sub_img_0'] and basemerchandise_object.sub_img_0:
                s3_client.delete_object(Bucket=os.environ.get('AWS_BUCKET_NAME'), Key=f'{(basemerchandise_object.sub_img_0).split(s3_address)[1]}')
            if files['sub_img_1'] and basemerchandise_object.sub_img_1:
                s3_client.delete_object(Bucket=os.environ.get('AWS_BUCKET_NAME'), Key=f'{(basemerchandise_object.sub_img_1).split(s3_address)[1]}')
            if files['sub_img_2'] and basemerchandise_object.sub_img_2:
                s3_client.delete_object(Bucket=os.environ.get('AWS_BUCKET_NAME'), Key=f'{(basemerchandise_object.sub_img_2).split(s3_address)[1]}')
            for i, key in enumerate(files.keys()):
                s3_path = f'{common_code}/No0{i+1}/{files[key]}'
                if files[key]:
                    s3_client.upload_fileobj(files[key], os.environ.get('AWS_BUCKET_NAME'), s3_path, ExtraArgs = {"ContentType": 'image/jpeg'})
                    s3_url = os.environ.get('AWS_S3_ADDRESS') + s3_path
                    request.data[key] = s3_url
            self.partial_update(request, *args, **kwargs)
            response = {}
            response['message'] = 'SUCCESSFULLY UPDATE MERCHANDISE'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=201)
        except:
            response = {}
            response['message'] = 'UPDATE FAIL'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=400)
    
    
    @csrf_exempt
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer access_token", type=openapi.TYPE_STRING)])
    def delete(self, request, *args, **kwargs):
        '''
            empty
            
            ---
        '''
        
        response = JWTAuthentication().authenticate(request)
        if response:
            user, token = response
        
        if User.objects.get(id=str(user)).is_superuser is False:
            return JsonResponse({'error': 'SUPERUSER AUTHENTICATION ERROR'}, status=403)
        
        try:
            s3_client = boto3.client('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
            s3_address = os.environ.get('AWS_S3_ADDRESS')
            basemerchandise_object = self.get_object()
            if basemerchandise_object.main_img:
                s3_client.delete_object(Bucket=os.environ.get('AWS_BUCKET_NAME'), Key=f'{(basemerchandise_object.main_img).split(s3_address)[1]}')
            if basemerchandise_object.sub_img_0:
                s3_client.delete_object(Bucket=os.environ.get('AWS_BUCKET_NAME'), Key=f'{(basemerchandise_object.sub_img_0).split(s3_address)[1]}')
            if basemerchandise_object.sub_img_1:
                s3_client.delete_object(Bucket=os.environ.get('AWS_BUCKET_NAME'), Key=f'{(basemerchandise_object.sub_img_1).split(s3_address)[1]}')
            if basemerchandise_object.sub_img_2:
                s3_client.delete_object(Bucket=os.environ.get('AWS_BUCKET_NAME'), Key=f'{(basemerchandise_object.sub_img_2).split(s3_address)[1]}')
            self.destroy(request, *args, **kwargs)
            response = {}
            response['message'] = 'SUCCESSFULLY DELETE MERCHANDISES'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=201)
        except:
            response = {}
            response['message'] = 'DELETE FAIL'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=404)


class SuperuserOptionMerchandiseUpdateDeleteView(UpdateAPIView, DestroyAPIView):
    
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    queryset = Merchandise.objects.all()
    serializer_class = SellerMerchandiseUpdateSerializer
    
    @csrf_exempt
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer access_token", type=openapi.TYPE_STRING)])
    def patch(self, request, *args, **kwargs):
        '''
            empty
            
            ---
        '''
        
        user, token = JWTAuthentication().authenticate(request)
        if User.objects.get(id=str(user)).is_superuser is False:
            return JsonResponse({'error': 'SUPERUSER AUTHENTICATION ERROR'}, status=403)
        
        try:
            self.partial_update(request, *args, **kwargs)
            response = {}
            response['message'] = 'SUCCESSFULLY UPDATE MERCHANDISE OPTION'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=201)
        except:
            response = {}
            response['message'] = 'UPDATE FAIL'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=400)
    
    
    @csrf_exempt
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer access_token", type=openapi.TYPE_STRING)])
    def delete(self, request, *args, **kwargs):
        '''
            empty
            
            ---
        '''
        
        response = JWTAuthentication().authenticate(request)
        if response:
            user, token = response
        
        if User.objects.get(id=str(user)).is_superuser is False:
            return JsonResponse({'error': 'SUPERUSER AUTHENTICATION ERROR'}, status=403)
        
        try:
            self.destroy(request, *args, **kwargs)
            response = {}
            response['message'] = 'SUCCESSFULLY DELETE MERCHANDISE OPTION'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=201)
        except:
            response = {}
            response['message'] = 'DELETE FAIL'
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=404)