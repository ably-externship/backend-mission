from missions.week_1.back.api import BaseView


class UserBaseView(BaseView):
    pass


class LoginView(UserBaseView):
    pass


class LogoutView(UserBaseView):
    pass


class RegisterView(UserBaseView):
    _db = 'meta'
    _table = 'customer'
    pass