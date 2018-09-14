from django.db import models

from .product import Product


class ProductOptionManager(models.Manager):
    def create(self, **kwargs):
        if not ('unit' in kwargs and 'price' in kwargs):
            raise ValueError('"unit" and "price" keyword arguments required')
        return super().create(**kwargs)


class ProductOption(models.Model):
    """
    RelatedManagers
    - unit_set (ProductOptionUnit)
    - price_set (ProductOptionPrice)
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='상품',
        related_name='option_set',
    )
    title = models.CharField('옵션명', max_length=200)

    objects = ProductOptionManager()

    class Meta:
        verbose_name = '상품 옵션'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return '상품 옵션 ({product} - {option})'.format(
            product=self.product.title,
            option=self.title,
        )

    def __init__(self, *args, **kwargs):
        """
        unit과 price값이 self.model(**kwargs)와 같은 방식으로 주어졌을 때,
        save()에서 해당 값들을 사용할 수 있도록 인스턴스에 저장해놓음
        :param args:
        :param kwargs:
        """
        self._unit = kwargs.pop('unit', None)
        self._price = kwargs.pop('price', None)
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        """
        save()에 직접 'unit', 'price'를 전달받거나
        ProductOption(unit=..., price=...)형태로 받은 경우 모두 처리
        :param args:
        :param kwargs:
        :return:
        """
        unit = kwargs.get('unit', self._unit)
        price = kwargs.get('price', self._price)
        if self.pk:
            super().save(*args, **kwargs)
        else:
            if not (unit and price):
                raise ValueError('Argument "unit" and "price" are required to create ProductOption')
            super().save(*args, **kwargs)
        # 모델 변경사항 저장 후 unit, price관련 값 설정
        instance = self.__class__.objects.get(pk=self.pk)
        instance.unit = unit
        instance.price = price

    @property
    def unit(self):
        if self.pk and not self.unit_set.exists():
            self.unit_set.create(unit=1)
        return self.unit_set.first().unit

    @unit.setter
    def unit(self, value):
        if self.unit != value:
            self.unit_set.create(unit=value)

    @property
    def price(self):
        if not self.price_set.exists():
            self.price_set.create(price=0)
        return self.price_set.first().price

    @price.setter
    def price(self, value):
        if self.price != value:
            self.price_set.create(price=value)

    @property
    def price_per_unit(self):
        return self.price * self.unit


class ProductOptionUnit(models.Model):
    product_option = models.ForeignKey(
        ProductOption,
        verbose_name='상품옵션',
        related_name='unit_set',
        on_delete=models.CASCADE,
    )
    unit = models.PositiveIntegerField('단위수량', default=1)
    start_at = models.DateTimeField('적용일시', auto_now_add=True)

    class Meta:
        verbose_name = '상품옵션 단위수량'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ('-start_at',)

    def __str__(self):
        return '상품옵션 단위수량 ({product} - {option} [단위: {unit}, 기간: {start}{end}])'.format(
            product=self.product_option.product.title,
            option=self.product_option.title,
            unit=self.unit,
            start=self.start_at,
            end=f' ~ {self.next_unit.start_at}' if self.next_unit else '',
        )

    @property
    def next_unit(self):
        return self.product_option.unit_set.filter(start_at__gt=self.start_at).first()


class ProductOptionPrice(models.Model):
    """
    상품의 가격이 변했을 때, 기존 주문들의 가격은 그대로 유지시키기 위해 기간별 Price정보만 따로 기재
    """
    product_option = models.ForeignKey(
        ProductOption,
        verbose_name='상품옵션',
        related_name='price_set',
        on_delete=models.CASCADE,
    )
    price = models.DecimalField('가격', max_digits=12, decimal_places=1, default=0)
    start_at = models.DateTimeField('적용일시', auto_now_add=True)

    class Meta:
        verbose_name = '상품옵션 가격'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ('-start_at',)

    def __str__(self):
        return '상품옵션 가격 ({product} - {option}, [가격: {price}, 기간: {start}{end}]'.format(
            product=self.product_option.product.title,
            option=self.product_option.title,
            price=self.price,
            start=self.start_at,
            end=f' ~ {self.next_price.start_at}' if self.next_price else '',
        )

    @property
    def next_price(self):
        """
        이 상품가격의 다음 시점
        :return:
        """
        return self.product_option.price_set.filter(start_at__gt=self.start_at).first()
