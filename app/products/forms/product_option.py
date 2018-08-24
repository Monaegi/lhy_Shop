from django import forms
from ..models import ProductOption


class ProductOptionForm(forms.ModelForm):
    unit = forms.IntegerField(label='단위수량')
    price = forms.DecimalField(label='가격')

    class Meta:
        model = ProductOption
        fields = (
            'product',
            'title',
            'unit',
            'price',
        )

    def __init__(self, *args, **kwargs):
        """
        ProductOption과 연결된 모델의 데이터인
        unit, price항목값을 채워줌

        :param args:
        :param kwargs:
        """
        if not kwargs.get('initial'):
            kwargs['initial'] = {}
        instance = kwargs.get('instance')
        if instance:
            kwargs['initial'].update({
                'unit': instance.unit,
                'price': instance.price,
            })
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        """
        cleaned_data에 전달된 unit, price값을 모델의 save()에 전달
        :param args:
        :param kwargs:
        :return:
        """
        option = super().save(*args, **kwargs)
        option.save(
            unit=self.cleaned_data['unit'],
            price=self.cleaned_data['price'],
        )
        return option
