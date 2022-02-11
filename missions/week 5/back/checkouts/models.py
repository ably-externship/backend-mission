import datetime

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from accounts.models import Address
from base.settings.common import AUTH_USER_MODEL
from products.models import ProductOption


class PaymentMethod(models.Model):
    name = models.CharField(max_length=16)
    pg = models.CharField(max_length=16)
    pay_method = models.CharField(max_length=8)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['order_id']),
        ]

    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    receipt_id = models.CharField(max_length=32, null=True, default=None)
    order_id = models.CharField(max_length=32, unique=True)
    method = models.ForeignKey(PaymentMethod, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    amount = models.BigIntegerField('금액')
    status = models.CharField(max_length=10, default='ready', choices=[
        ('ready', '준비'), ('paid', '완료'), ('failed', '실패'), ('cancelled', '취소')
    ])
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def create_transaction(user: AUTH_USER_MODEL, method: PaymentMethod, name: str, amount: int,
                           address: Address) -> models.Model:
        order_id = hex(user.id % 16)[-1].upper() + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        transaction = Transaction(user=user, order_id=order_id, method=method, name=name, amount=amount,
                                  address=address)
        transaction.save()
        return transaction

    def __str__(self):
        return self.order_id


class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product_option = models.ForeignKey(ProductOption, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    unit_price = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_price(self):
        return self.unit_price * self.quantity

    def __str__(self):
        return f'{self.product_option.product.display_name} {self.product_option} {self.quantity}'
