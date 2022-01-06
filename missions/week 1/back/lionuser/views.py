from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .forms import LoginForm, RegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Lionuser
from .serializers import UserLoginSerializer
# Create your views here.

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):

        user = Lionuser(
            email=form.data.get('email'),
            password=form.data.get('password') #makepassrowd
            #level='user'
        )
        user.save()

        return super().form_valid(form)

    val = {'response': 'User Added'}
    JsonResponse(val, status=200)

from rest_framework_jwt.settings import api_settings

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
from django.contrib.auth import authenticate





@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        # if serializer.validated_data['email'] == "None": # email required
        #     return Response({'message': 'fail'}, status=status.HTTP_200_OK)
        response = {
            'success': True,
            'token': serializer.data['token'] # 시리얼라이저에서 받은 토큰 전달
        }
        return JsonResponse(response, status=status.HTTP_200_OK)

@csrf_exempt
def userLogin(request):
    if request.method == 'GET':
        return render(request,'login.html')



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])


def loginTest(request):
    print(request.META.get('HTTP_AUTHORIZATION'))
    if request.method == 'GET':
        return JsonResponse({"Success":"header에 jwt token으로 api 요청 성공"})

