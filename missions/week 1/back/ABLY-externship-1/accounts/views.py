from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import request, HttpResponseRedirect
from django.shortcuts import resolve_url
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView
from django.shortcuts import redirect, render
from .forms import SignupForm
from products.views import MerchandiseALL


# Create your views here.


class UserSignup(RedirectView):
    
    def get(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                signed_user = form.save()
                login(request, signed_user)
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
        else:
            form = SignupForm()
        
        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context)


class UserLogin(LoginView):
    
    next_page = 'home'
    template_name = 'accounts/login.html'
    redirect_authenticated_user = False
    
    def __init__(self, **kwargs):
        try:
            if request.user:
                self.redirect_authenticated_user = True
        except:
            pass
        super().__init__(**kwargs)
    
    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        return resolve_url(self.next_page)
    
    def get_success_url(self):
        return self.get_default_redirect_url()
    
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        request.user = form.get_user()
        return super().form_valid(form)

