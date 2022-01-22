from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.http import Http404


class LoggedInOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy("login_page")


class LoggedOutOnlyView(UserPassesTestMixin):

    permission_denied_message = "Page Not Found"

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there")
        return redirect(reverse("home_page"))


class EmailLoginOnlyView(UserPassesTestMixin):

    permission_denied_message = "Page Not Found"

    def test_func(self):
        return self.request.user.login_method == "email"

    def handle_no_permission(self):
        raise Http404("Page not found")


class HostOnlyView(UserPassesTestMixin):

    permission_denied_message = "Page Not Found"

    def test_func(self):
        return self.request.session.get("is_hosting")

    def handle_no_permission(self):
        raise Http404("Page not found")