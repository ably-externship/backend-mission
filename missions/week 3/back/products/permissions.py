from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    custom permission to only allow staff to edit it.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to staff
        return request.user.is_staff


class IsVendorOrReadOnly(permissions.BasePermission):
    """
    custom permission to only allow the vendor of the product to edit it.
    """

    def has_product_permission(self, request, view, product):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the vendor of the product.
        return product.vendor == request.user