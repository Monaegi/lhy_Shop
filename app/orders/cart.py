from django.conf import settings

from products.models import ProductOption


class CartItemNotExist(Exception):
    def __init__(self, product_option, *args):
        super().__init__(*args)
        self.msg = f'{product_option.title} is not exist'

    def __str__(self):
        return self.msg


class CartItem:
    def __init__(self, product_option_pk, quantity):
        self.product_option = ProductOption.objects.get(pk=product_option_pk)
        self.quantity = quantity

    @property
    def product(self):
        return self.product_option.product


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(settings.CART_SESSION_ID, {})

        not_exist_pk_list = []
        for key in self.cart:
            if not ProductOption.objects.values('pk').filter(pk=key).exists():
                not_exist_pk_list.append(key)
        for not_exist_pk in not_exist_pk_list:
            del self.cart[not_exist_pk]

    def add(self, product_option, quantity):
        product_option_pk = str(product_option.pk)
        self.cart.setdefault(product_option_pk, {'quantity': 0})['quantity'] += quantity
        self.save()

    def remove(self, product_option):
        product_option_pk = str(product_option.pk)
        if product_option_pk not in self.cart:
            raise CartItemNotExist(product_option)
        del self.cart[product_option_pk]
        self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        print(self.session[settings.CART_SESSION_ID])
        self.session.modified = True

    @property
    def items(self):
        return [CartItem(pk, item['quantity']) for pk, item in self.cart.items()]

    def __iter__(self):
        for item in self.items:
            yield item

    def __len__(self):
        return len(self.cart)

    def get_item_price(self, product_option_pk):
        quantity = self.cart[product_option_pk]['quantity']
        return ProductOption.objects.get(pk=product_option_pk).price_per_unit * quantity

    @property
    def amount(self):
        return sum([self.get_item_price(pk) for pk in self.cart.keys()])
