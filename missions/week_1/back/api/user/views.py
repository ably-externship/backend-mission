from ..views import BaseView


class UserBaseView(BaseView):
    pass


class Test:
    @classmethod
    def test(cls):
        print(1)
        return None


class LoginView(UserBaseView):
    pass


class LogoutView(UserBaseView):
    pass


class RegisterView(UserBaseView):
    _db = 'meta'
    _table = 'customer'
    pass