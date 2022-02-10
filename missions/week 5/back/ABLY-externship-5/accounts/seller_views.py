from .models import User, Seller
from django.forms.models import model_to_dict
from django.db import transaction, IntegrityError
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenViewBase, TokenObtainPairView
from rest_framework_simplejwt.authentication import AUTH_HEADER_TYPES
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import re


# Create your views here.
def check_username_duplication(username):
    
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'INVALID USERNAME, ALREADY USED'}, status=400)
    
    return None


def check_phone_duplication(phone_number):
    
    if Seller.objects.filter(phone_number=phone_number).exists():
        return JsonResponse({'error': 'INVALID PHONE NUMBER, ALREADY USED'}, status=400)
    
    return None


def check_email_duplication(email):
    
    if User.objects.filter(email=email).exists():
        return JsonResponse({'error': 'INVALID EMAIL, ALREADY USED'}, status=400)
    
    return None


def check_password_validation(password):
    
    if len(password)>int(16) or len(password)<int(8):
        return JsonResponse({'error': 'INVALID PASSWORD, PLEASE CHECK PASSWORD LENGTH'}, status=400)
    
    if re.search('[`~!@#$%^&*(),<.>/?]+', password) is None:
        return JsonResponse({'error': 'INVALID PASSWORD, PLEASE CHECK PASSWORD INCLUDES SPECIAL LETTER'}, status=400)
    
    if re.search('[0-9]', password) is None:
        return JsonResponse({'error': 'INVALID PASSWORD, PLEASE CHECK PASSWORD INCLUDES NUMBER'}, status=400)
    
    if re.search('[a-z]', password) is None:
        return JsonResponse({'error': 'INVALID PASSWORD, PLEASE CHECK PASSWORD INCLUDES SMALL LETTER'}, status=400)
    
    if re.search('[A-Z]', password) is None:
        return JsonResponse({'error': 'INVALID PASSWORD, PLEASE CHECK PASSWORD INCLUDES LARGE LETTER'}, status=400)
    
    return None


def check_username_password_correct(username, password):
    
    if not User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'ACCOUNT NOT EXIST, PLEASE CHECK YOUT ID'}, status=404)
    
    encoded_password = User.objects.get(username=username).password
    response = check_password(password, encoded_password, setter=None, preferred='default')
    
    if response is False:
        return JsonResponse({'error': 'PLEASE CHECK YOUR PASSWORD'}, status=404)
    
    return None


class SellerSignupView(TokenObtainPairView, TokenViewBase):
    '''
        seller sign up
        
        ---
    '''
    
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer
    
    www_authenticate_realm = 'api'
    
    def get_authenticate_header(self, request):
        return '{0} realm="{1}"'.format(AUTH_HEADER_TYPES[0], self.www_authenticate_realm)
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        
        try:
            username = request.data['username']
            password = request.data['password']
            email = request.data['email']
            phone_number = request.data['phone_number']
            brand = request.data['brand']
        except KeyError:
            return JsonResponse({'error': 'SIGNUP KEY ERROR'}, status=400)
        
        check_response = check_username_duplication(username=username)
        if check_response:
            return check_response
        check_response = check_phone_duplication(phone_number)
        if check_response:
            return check_response
        check_response = check_email_duplication(email)
        if check_response:
            return check_response
        check_response = check_password_validation(password=password)
        if check_response:
            return check_response
        password = make_password(password=password, salt=None, hasher='default')
        
        try:
            with transaction.atomic():
                user_object = User.objects.create(username=username, password=password, email=email)
                seller_objcet = Seller.objects.create(user=user_object, phone_number=phone_number, brand=brand)
                serializer = self.get_serializer(data=request.data)
        except IntegrityError:
            pass
        
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        response = {}
        response['message'] = 'SUCCESSFULLY SIGNED UP'
        response['account'] = model_to_dict(seller_objcet)
        response['token'] = serializer.validated_data
        
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=201)


class SellerSigninView(TokenObtainPairView, TokenViewBase):
    '''
        sign in
        
        ---
    '''
    
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer
    
    www_authenticate_realm = 'api'
    
    def get_authenticate_header(self, request):
        return '{0} realm="{1}"'.format(AUTH_HEADER_TYPES[0], self.www_authenticate_realm)
    
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        
        try:
            username = request.data['username']
            password = request.data['password']
        except KeyError:
            return JsonResponse({'error': 'SIGNIN KEY ERROR'}, status=400)
        
        check_response = check_username_password_correct(username, password)
        if check_response:
            return check_response
        
        seller_object = User.objects.prefetch_related('seller').get(username=username).seller
        
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        response = {}
        response['message'] = 'SUCCESSFULLY SIGNED IN'
        response['account'] = model_to_dict(seller_object)
        response['token'] = serializer.validated_data
        
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=200)


class TokenRefreshView(TokenViewBase):
    '''
        token refresh
        
        ---
    '''
    
    permission_classes = [AllowAny]
    serializer_class = serializer_class = TokenRefreshSerializer
    
    www_authenticate_realm = 'api'
    
    def get_authenticate_header(self, request):
        return '{0} realm="{1}"'.format(AUTH_HEADER_TYPES[0], self.www_authenticate_realm)
    
    @csrf_exempt
    @swagger_auto_schema(manual_parameters=[openapi.Parameter('Authorization', openapi.IN_HEADER, description="Bearer refresh_token", type=openapi.TYPE_STRING)])
    def post(self, request, *args, **kwargs):
        
        try:
            refresh = request.data['refresh']
        except KeyError:
            return JsonResponse({'error': 'TOKEN KEY ERROR'}, status=400)
        
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        response = {}
        response['message'] = 'SUCCESSFULLY TOKEN REFRESHED'
        response['token'] = serializer.validated_data
        
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, status=200)