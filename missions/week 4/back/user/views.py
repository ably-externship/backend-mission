from django.shortcuts import render, redirect, reverse, get_object_or_404
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
from allauth.socialaccount.models import SocialAccount


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
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password, email=email)
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


# 유저 프로필 페이지 -----
@login_required(login_url='login')
def user_profile(request):
    is_social = SocialAccount.objects.filter(user_id=request.user).exists()
    return render(request, 'user/profile.html', {'is_social':is_social})

# 유저 프로필 변경 페이지 -----
@login_required(login_url='login')
def profile_update_page(request):
    is_social = SocialAccount.objects.filter(user_id=request.user).exists()
    is_profiled = UserProfile.objects.filter(user_id=request.user).exists()
    user = User.objects.get(id=request.user.id)

    if is_profiled:
        user_profile = UserProfile.objects.get(user_id=request.user.id)
        return render(request, 'user/update.html', {'user':user, 'user_profile':user_profile, 'is_social':is_social, 'is_profiled':is_profiled})
    else:
        return render(request, 'user/update.html', {'user':user, 'is_social':is_social, 'is_profiled':is_profiled})


# 유저 프로필 변경 -----
@login_required(login_url='login')
def profile_update(request):
    is_profiled = UserProfile.objects.filter(user_id=request.user.id).exists()

    if request.method == 'POST':
        # 프로필 처음 등록할 시---
        if is_profiled == False:
            selected_user = User.objects.get(id=request.user.id)
            real_name = request.POST['realname']
            selected_user.first_name = real_name
            selected_user.save()

            UserProfile.objects.create(user_id=selected_user.id,
                                        phone = request.POST['phone'],
                                       address=request.POST['address']
                                       )

            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        # 빈칸으로 등록할 때 기존 사항 유지---
        elif request.POST['realname']=="" or request.POST['phone']=="" or request.POST['address']=="":
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        # 등록된 프로필 수정 시---
        else:
            selected_user = User.objects.get(id=request.user.id)
            real_name = request.POST['realname']
            selected_user.first_name = real_name
            selected_user.save()

            userprofile = UserProfile.objects.get(user_id=request.user)
            phone = request.POST['phone']
            address = request.POST['address']
            userprofile.phone=phone
            userprofile.address=address
            userprofile.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
