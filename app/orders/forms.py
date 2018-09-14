from django import forms

from products.models import ProductOption
from .cart import Cart

__all__ = (
    'CartItemAddForm',
    'CartItemRemoveForm',
)


class CartItemFormMixin(forms.Form):
    product_option = forms.IntegerField()

    def clean_product_option(self):
        data = self.cleaned_data['product_option']
        if not ProductOption.objects.filter(pk=data).exists():
            raise forms.ValidationError(f'ProductOption(PK:{data}) not exist')
        return ProductOption.objects.get(pk=data)

    def save(self, *args, **kwargs):
        if not self.is_valid():
            raise forms.ValidationError('Save must execute after is_valid()')


class CartItemAddForm(CartItemFormMixin, forms.Form):
    quantity = forms.IntegerField()

    def save(self, request):
        super().save(request)
        cart = Cart(request)
        cart.add(
            product_option=self.cleaned_data['product_option'],
            quantity=self.cleaned_data['quantity'],
        )
        return cart


class CartItemRemoveForm(CartItemFormMixin, forms.Form):
    def save(self, request):
        super().save(request)
        cart = Cart(request)
        cart.remove(product_option=self.cleaned_data['product_option'])
        return cart
