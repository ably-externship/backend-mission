from django.http import HttpResponseForbidden

from accounts.models import User


def account_owner(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
