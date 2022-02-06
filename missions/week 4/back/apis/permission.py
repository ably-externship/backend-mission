from rest_framework import permissions
from rest_framework.permissions import BasePermission


# 4주차
class MasterSerializer(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'brand')


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.brand_master == request.user.profile
