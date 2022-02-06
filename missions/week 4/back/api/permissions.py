from rest_framework import permissions
from shop.models import Shop


class IsShopAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 요청자(request.user)가 객체(Product)의 user와 동일한지 확인
        try:
            user = Shop.objects.get(shop_id=request.user)
            if hasattr(obj, 'shop_id'):
                return obj.shop_id == user
            elif hasattr(obj, 'product_id'):
                return obj.product_id.shop_id == user
        except:
            return False