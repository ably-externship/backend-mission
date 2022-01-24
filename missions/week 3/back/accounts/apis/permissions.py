from rest_framework.permissions import BasePermission


class IsMarketAdmin(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'market')
