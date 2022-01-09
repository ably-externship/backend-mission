from django.db import models


class Order(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name="구매자")
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name="상품")
    quantity = models.IntegerField(verbose_name="수량")
    amount = models.PositiveIntegerField(verbose_name='결제금액')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="구매일자")

    def __str__(self):
        return '{} {}'.format(self.user, self.product)
