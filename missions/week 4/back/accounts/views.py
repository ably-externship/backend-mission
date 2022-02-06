from django.shortcuts import render
from django.contrib.auth.models import User  
from django.contrib import auth  
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# Create your views here.

@csrf_exempt
def signup(request):
  if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],password=request.POST['password1'])
            return redirect('index')

  return render(request, 'accounts/signup.html')

# def login(request):
  
#   return render(request, 'accouts/login.html')

@csrf_exempt
def forgot_id(request):
  if request.method == "POST":
    email = request.POST["email"]
    if email == "":
      messages.info(request, '이메일를 입력하지 않으셨습니다.')
      return render(request, 'accounts/find_id.html')
      
    else :
      try :
        user = User.objects.get(email=email)
        if user is not None:
          messages.info(request, '해당 이메일을 사용한 아이디는 :')
          messages.info(request, user.username)
          return render(request, 'accounts/find_id.html' )
        
      
      except :
        messages.info(request, '해당 이메일을 사용한 아이디가 없습니다.')
        return render(request, 'accounts/find_id.html')
    
  else :
    return render(request, 'accounts/find_id.html')
    