from rest_framework import permissions

from products.models import Product


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    조회는 인증여부 없이 가능
    제품옵션 생성, 수정, 삭제는 브랜드 주인만 가능
    관리자는 모두 가능 (django admin page 접속 가능한 사람)
    """

    # /products
    def has_permission(self, request, view) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        product_id = request.resolver_match.kwargs.get('pk')
        product_owner = Product.objects.get(id=product_id).market.owner
        return (request.user == product_owner) or request.user.is_staff

    # /products/<id>
    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        product_id = request.resolver_match.kwargs.get('pk')
        product_owner = Product.objects.get(id=product_id).market.owner
        return (request.user == product_owner) or request.user.is_staff
