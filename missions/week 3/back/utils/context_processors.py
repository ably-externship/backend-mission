from cart.models import *
from django.contrib.auth.decorators import login_required

# 카트 담긴 상품 수 표시 -----
def notification(request):
    if request.user.is_authenticated:
        current_user = request.user
        numbers = Cart.objects.filter(user_id=current_user)
        number = len(numbers)
    else:
        number = None
    return {'number': number,}