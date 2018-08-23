from django.db import models

from .product_category import (
    ProductCategory,
)


class Product(models.Model):
    """
    RelatedManagers
    - option_set (ProductOption)
    """
    category = models.ForeignKey(
        ProductCategory,
        verbose_name='카테고리',
        related_name='product_set',
        on_delete=models.CASCADE,
    )
    title = models.CharField('상품명', max_length=100)

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ('title',)

    def __str__(self):
        return f'상품 ({self.title})'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
