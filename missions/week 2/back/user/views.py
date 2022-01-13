from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.views import PasswordResetView
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
import requests

# 회원가입
def signup(request):
    if request.method =="POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                                            username=request.POST["username"],
                                            # phone=request.POST["phone"],
                                            email=request.POST["email"],
                                            password=request.POST["password1"],)
            auth.login(request,user)
            return redirect('/')
        else:
            print("비밀번호가 다릅니다.")
        return render(request, 'signup.html')
    return render(request,'signup.html')

# 로그인
def login(request):
    print("333", request.session.modified)

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("로그인 성공")
            return redirect('/')
        else:
            print("로그인 실패")
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})
    else:
        return render(request,'login.html')


def index(request):
    print('1111',request)
    _context = {'check':False}
    if request.session.get('access_token'):
        _context['check'] = True
    return render(request, 'login.html', _context)

def kakaoLoginLogic(request):
    _restApiKey = '043437c8945b496dc9d65e0d6d94135d' # 입력필요
    _redirectUrl = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApiKey = '043437c8945b496dc9d65e0d6d94135d' # 입력필요
    _redirect_uri = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    print("222",request.session.modified)
    return render(request, 'loginSuccess.html')

def kakaoLogout(request):
    print("444", request.session.modified)
    _token = request.session['access_token']
    # _url = 'https://kapi.kakao.com/v1/user/logout'
    # _header = {
    #   'Authorization': f'bearer {_token}'
    # }
    _url = 'https://kapi.kakao.com/v1/user/unlink'
    _header = {
      'Authorization': f'bearer {_token}',
    }
    _res = requests.post(_url, headers=_header)
    _result = _res.json()
    if _result.get('id'):
        print("5555",request.session['access_token'])
        del request.session['access_token']
        print("6666",request.session)
        return render(request, 'loginoutSuccess.html')
    else:
        return render(request, 'logoutError.html')

# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('/')

# 아이디 찾기
def ForgotIDView(request):
    context={}
    if request.method=='POST':
        email=request.POST.get('email')
        try:
            user=User.objects.get(email=email)
            if user is not None:
                method_email=EmailMessage('Your ID is in the email',
                                          str(user.username),
                                          settings.EMAIL_HOST_USER,
                                          [email],
                                          )
            method_email.send(fail_silently=False)
            return render(request,'login.html',context)
        except:
            messages.info(request,"there is no username along with the email")
    context={}
    return render(request,'forgotID.html',context)

# 비밀번호 초기화
class UserPasswordResetView(PasswordResetView):
    template_name = 'resetPW.html'

    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            opts = {
                'use_https': self.request.is_secure(),
                'token_generator': self.token_generator,
                'from_email': self.from_email,
                'email_template_name': self.email_template_name,
                'subject_template_name': self.subject_template_name,
                'request': self.request,
                'html_email_template_name': self.html_email_template_name,
                'extra_email_context': self.extra_email_context,
            }
            form.save(**opts)
            return render(self.request,'login.html')
        else:
            return render(self.request, 'password_reset_done_fail.html')