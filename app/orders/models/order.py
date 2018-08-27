from django.conf import settings
from django.db import models

from utils.classes.models import TimeStampedModel

__all__ = (
    'Order',
    'OrderItem',
)


class Order(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='주문자',
        on_delete=models.SET_NULL,
        null=True,
    )


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(
        Order,
        verbose_name='주문내역',
        on_delete=models.CASCADE,
    )
    product_option = models.ForeignKey(
        'products.ProductOption',
        verbose_name='상품 옵션',
        on_delete=models.SET_NULL,
        null=True
    )
    quantity = models.PositiveSmallIntegerField('수량')
