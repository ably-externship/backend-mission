from rest_framework import permissions

from product.models import Product


class IsAuthor(permissions.BasePermission):

    # def has_permission(self, request, view):
    #
    #     qs = Product.objects.filter(author=request.user)
    #     data = list(qs)
    #     data = ''.join(map(str, data))
    #     data = data.split('::')
    #
    #
    #     return False

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user