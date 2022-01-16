from venv import create
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.http import request, HttpResponseRedirect
from django.shortcuts import resolve_url
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView
from django.views import View
from django.db import transaction
from django.shortcuts import redirect, render
from .forms import SignupForm
from .models import User, Customer, Seller
from .socials import SocialLoginProfile
from .tokens import jwt_publish, jwt_authorization
import os
# from products.views import MerchandiseALL


# Create your views here.


class UserSignup(RedirectView):
    
    def get(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                password = str(request.POST['password1'])
                password = make_password(password=password, salt=None, hasher='default')
                with transaction.atomic():
                    signed_user = User.objects.create(
                        username=str(request.POST['username']),
                        password=password,
                        email=str(request.POST['email'])
                    )
                    Customer.objects.create(
                        user=signed_user,
                        phone_number=str(request.POST['phone_number']),
                        is_local=True
                    )
                access_jwt = jwt_publish(str(signed_user)) # bcrypt ImportError: mac m1 issue
                response = HttpResponseRedirect('/')
                response.set_cookie(
                    key='_utk',
                    value=access_jwt
                )
                return response
        else:
            form = SignupForm()
        
        context = {
            'form': form
        }
        cnt = request.session.get('test_session')
        cnt = int(cnt)
        cnt += 1
        request.session['test_session'] = cnt
        return render(request, 'accounts/signup.html', context)


class UserLogin(LoginView):
    
    next_page = 'home'
    template_name = 'accounts/login.html'
    redirect_authenticated_user = False
    
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)
    
    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        return resolve_url(self.next_page)
    
    def get_success_url(self):
        return self.get_default_redirect_url()
    
    def form_valid(self, form):
        access_jwt = jwt_publish(str(form.get_user())) # bcrypt ImportError: mac m1 issue
        response = HttpResponseRedirect(self.get_success_url())
        response.set_cookie(
            key='_utk',
            value=access_jwt
        )
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            self.redirect_field_name: self.get_redirect_url(),
            'site': current_site,
            'site_name': current_site.name,
            'kakao_client_id': os.environ.get('KAKAO_CLIENT_ID'),
            **(self.extra_context or {})
        })
        return context


class SocialLogin(View):
    
    def get(self, request, *args, **kwargs):
        try:
            data = SocialLoginProfile.kakao(request, request.GET['code'])
            phone_number = data['phone_number']
            social_type = 'kakao'
            social_id = make_password(password=data['social_id'], salt=None, hasher='default') # bcrypt ImportError: mac m1 issue
        except:
            messages.error(request, 'KAKAO LOGIN FAIL')
            return redirect('login')
        
        if Customer.objects.filter(phone_number=phone_number):
            Customer.objects.filter(phone_number=phone_number).update(
                connect_social=True,
                social_type=social_type,
                social_id=social_id
            )
            user = Customer.objects.get(phone_number=phone_number).user
        elif Customer.objects.filter(social_id=social_id):
            user = Customer.objects.filter(social_id=social_id).user
        else:
            with transaction.atomic():
                signed_user = User.objects.create(
                    username=social_id,
                    password=None
                )
                Customer.objects.create(
                    user=signed_user,
                    phone_number=phone_number,
                    connect_social=True,
                    social_type=social_type,
                    social_id=social_id
                )
                user = signed_user
        access_jwt = jwt_publish(str(user)) # bcrypt ImportError: mac m1 issue
        response = HttpResponseRedirect('/')
        response.set_cookie(
            key='_utk',
            value=access_jwt
        )
        return response


class UserLogout(View):
    
    @jwt_authorization
    def get(self, request, *args, **kwargs):
        access_jwt = jwt_publish('anonymoususer')
        response = HttpResponseRedirect('/')
        response.set_cookie(
            key='_utk',
            value=access_jwt
        )
        return response