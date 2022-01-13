from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from contents.models import Comment, Cart

# csrf 비활성화, 비로그인 사용자 접근제한
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# auth 인증 및 로그인, 로그아웃
from django.contrib.auth import authenticate, login, logout

# json 데이터 전달
from django.http import JsonResponse

# 에러 및 검증
from django.db import IntegrityError
from django.core.validators import validate_email, ValidationError

# 비로그인자 제한
from django.contrib.auth.decorators import login_required


# Create your views here.
# Base Api View -> 상속 부모
@method_decorator(csrf_exempt, name="dispatch")
class BaseView(View):
    @staticmethod
    def response(data={}, message='', status=200):
        result = {
            'data': data,
            'message': message,
        }
        return JsonResponse(result, status=status)


# 로그인 뷰
class UserLoginView(BaseView):
    def post(self, request):
        username = request.POST.get('username', '')
        if not username:
            return self.response(message='아이디를 입력해 주세요.', status=400)
        password = request.POST.get('password', '')
        if not password:
            return self.response(message='비밀번호를 입력해 주세요.', status=400)

        # authenticate 함수는 username, password가 일치하지 않을경우, None을 반환.
        user = authenticate(request, username=username, password=password)
        if user is None:
            return self.response(message='아이디 또는 비밀번호가 일치하지 않습니다.', status=400)
        login(request, user)

        return self.response()


# 회원가입
class UserCreateView(BaseView):
    # post 입력 처리 및 검증 구현
    def post(self, request):
        username = request.POST.get('username', '')
        if not username:
            return self.response(message='아이디를 입력해 주세요.', status=400)
        password = request.POST.get('password', '')
        if not password:
            return self.response(message='비밀번호를 입력해 주세요.', status=400)
        email = request.POST.get('email', '')
        try:
            validate_email(email)
        except ValidationError:
            return self.response(message='이메일을 입력해 주세요.', status=400)

        # 예외 처리
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return self.response(message='이미 존재하는 아이디 입니다.', status=400)

        return self.response({'user.id': user.id})


# 로그아웃 뷰
class UserLogoutView(BaseView):
    def get(self, request):
        logout(request)
        return self.response()


# # 아이디 찾기
# class UserForgotView(BaseView):
#     def post(self, request):
#         email = request.POST.get('email', '')
#         # 이메일을 입력하였는지 확인
#         if not email:
#             return self.response(message='이메일을 입력해 주세요.', status=400)
#
#         # 이메일이 유효한지 검증
#         try:
#             validate_email(email)
#         except ValidationError:
#             return self.response(message='잘못된 이메일 방식입니다.', status=400)
#
#         # 입력한 이메일과 일치하는 username 찾기
#         try:
#             user = User.oobjects.get(email=email)
#             if user is not None:


# 질문 생성 뷰
@method_decorator(login_required, name='dispatch')
class CommentCreateView(BaseView):
    def post(self, request):
        pk = request.POST.get('pk', '')
        content = request.POST.get('content', '')

        Comment.objects.create(product_id=pk, author=request.user, content=content)

        return self.response({})


# 장바구니 담기 뷰
@method_decorator(login_required, name='dispatch')
class CartAddView(BaseView):
    def post(self, request):
        product_id = request.POST.get('pk', '')
        print(product_id)

        try:
            cart = Cart.objects.get(product__id=product_id, user__id=request.user.id)
            if cart:
                if cart.product.id == product_id:
                    cart.quantity += 1
                    cart.save()
        except Cart.DoesNotExist:
            user = User.objects.get(id=request.user.id)
            cart = Cart.objects.create(
                user=user,
                product=product_id,
                quantity=1
            )
            cart.save()

        return self.response({})







