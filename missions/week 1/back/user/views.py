from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from argon2 import PasswordHasher, exceptions
from .forms import SignupForm
from .models import User


class SignupView(FormView):
    template_name = "user/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy('user:result')

    def form_valid(self, form):
        user_name = form.cleaned_data.get("user_name")
        user_id = form.cleaned_data.get("user_id")
        user_pw = form.cleaned_data.get("user_pw")
        user_email = form.cleaned_data.get("user_email")
        user = User.objects.create(user_name=user_name,
                                   user_id=user_id,
                                   user_pw=PasswordHasher().hash(user_pw),
                                   user_email=user_email)
        user.save()
        return super().form_valid(form)


def login(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user_pw = request.POST.get("user_pw")
        try:
            user = User.objects.get(user_id=user_id)
            if PasswordHasher().verify(user.user_pw, user_pw):  # db에 저장된 암호와 로그인 입력된 암호 검증
                request.session['user'] = user.user_id
                return redirect('product:main')
            # return JsonResponse({"message": "Login Success"}, status=200)

        except (User.DoesNotExist, exceptions.VerifyMismatchError):
            return redirect('user:login')

    else:
        return render(request, "user/login.html")


def logout(request):
    request.session.pop('user')
    return redirect('product:main')


def result(request):
    return render(request, 'user/success.html')

