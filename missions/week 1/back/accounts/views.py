from django.shortcuts import render
from django.contrib.auth.models import User  
from django.contrib import auth  
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def signup(request):
  if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('index')

  

  return render(request, 'accounts/signup.html')