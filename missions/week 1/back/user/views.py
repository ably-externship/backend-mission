from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from user.models import UserProfile
from user.forms import SignUpForm

# 이메일 보내기
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


@login_required(login_url='login')
def index(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'profile':profile}
    return render(request,'user_profile.html',context)

# 로그인 -----
def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user =request.user
            userprofile=UserProfile.objects.get(user_id=current_user.id)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"아이디 혹은 패스워드 오류입니다!")
            return HttpResponseRedirect('/login')
    context = {}
    return render(request, 'user/login.html', context)

# 회원가입 -----
def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.save()
            messages.success(request, '가입이 완료되었습니다. 로그인해주세요.')
            return HttpResponseRedirect('/login')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/join')

    form = SignUpForm()
    context = {'form': form,}
    return render(request, 'user/join.html', context)



# 비밀번호 메일 보내기 -----

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "user/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="user/password/password_reset.html", context={"password_reset_form":password_reset_form})