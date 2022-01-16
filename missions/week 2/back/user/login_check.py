from user.models import User
from django.shortcuts import render, redirect


def login_check(func):
    def wrapper(request, *args, **kwargs):
        try:
            user_id = request.session['user']
            user = User.objects.get(user_id=user_id)

        except (KeyError, User.DoesNotExist):
            context = {
                'message': '로그인이 필요한 기능입니다.'
            }
            return render(request, 'user/login.html', context=context)

        return func(request, *args, **kwargs)

    return wrapper
