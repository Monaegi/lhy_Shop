from django.db import models

from .product_category import (
    ProductCategorySmall,
)


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategorySmall,
        verbose_name='카테고리',
        related_name='products',
        on_delete=models.CASCADE,
    )
    title = models.CharField('상품명', max_length=100)

    def __str__(self):
        return '{top} > {middle} > {small} > {product}'.format(
            top=self.category.middle_category.top_category.title,
            middle=self.category.middle_category.title,
            small=self.category.title,
            product=self.title,
        )


class ProductPrice(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name='상품가격정보',
        related_name='prices',
        on_delete=models.CASCADE,
    )
    price = models.PositiveSmallIntegerField('가격', default=0)
    start_at = models.DateTimeField('적용일시', auto_now_add=True)

    def __str__(self):
        return '상품 가격 ({product}, {start}{end}'.format(
            product=self.product.title,
            start=self.start_at,
            end=f' ~ {self.next_price.start_at}' if self.next_price else '',
        )

    @property
    def next_price(self):
        """
        이 상품가격의 다음 시점
        :return:
        """
        return self.product.prices.filter(start_at__gt=self.start_at).first()
