from django.db import models

__all__ = (
    'ProductCategory',
)


class ProductCategory(models.Model):
    parent_category = models.ForeignKey(
        'self',
        verbose_name='상위 카테고리',
        on_delete=models.CASCADE,
        related_name='category_set',
        blank=True,
        null=True,
    )
    title = models.CharField('카테고리명', max_length=50)

    class Meta:
        verbose_name = '상품 카테고리'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return '{parent}{title}'.format(
            parent=f'{self.parent_category.__str__()} > ' if self.parent_category else '',
            title=self.title,
        )

    @property
    def is_top(self):
        return not bool(self.parent_category)

    @property
    def has_child(self):
        return self.category_set.exists()
