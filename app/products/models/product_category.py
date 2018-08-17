from django.db import models

__all__ = (
    'ProductCategoryTop',
    'ProductCategoryMiddle',
    'ProductCategorySmall',
)


class ProductCategoryTop(models.Model):
    title = models.CharField('카테고리명', max_length=50)

    class Meta:
        verbose_name = '최상위 카테고리'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.Meta.verbose_name} ({self.title})'


class ProductCategoryMiddle(models.Model):
    top_category = models.ForeignKey(
        ProductCategoryTop,
        verbose_name='최상위 카테고리',
        related_name='sub_categories',
        on_delete=models.CASCADE,
    )
    title = models.CharField('중분류명', max_length=50)

    class Meta:
        verbose_name = '중분류'
        verbose_name_plural = f'{verbose_name} 목록'
        order_with_respect_to = 'top_category'

    def __str__(self):
        return f'{self.top_category.title} > {self.title}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.sub_categories.exists():
            self.sub_categories.create(title='미분류')


class ProductCategorySmall(models.Model):
    middle_category = models.ForeignKey(
        ProductCategoryMiddle,
        verbose_name='중분류',
        related_name='sub_categories',
        on_delete=models.CASCADE,
    )
    title = models.CharField('소분류명', max_length=50)

    class Meta:
        verbose_name = '소분류'
        verbose_name_plural = f'{verbose_name} 목록'
        order_with_respect_to = 'middle_category'

    def __str__(self):
        return '{top} > {middle} > {small}'.format(
            top=self.middle_category.top_category.title,
            middle=self.middle_category.title,
            small=self.title,
        )
