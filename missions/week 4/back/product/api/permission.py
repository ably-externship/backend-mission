from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            True

        return obj.author == request.user
        # if hasattr(obj, 'product'):
        #     return obj.seller == request.user.seller

        # if obj.seller == request.user:
        #     return True
        #
        # return False

