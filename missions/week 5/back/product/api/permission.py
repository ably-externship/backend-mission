from rest_framework import permissions


class IsSellerorAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.user.is_staff:
            if request.method in permissions.SAFE_METHODS:
                return True
            if hasattr(obj, 'author'):
                return obj.author == request.user

        return False


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return obj.user == request.user
