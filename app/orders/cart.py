from django.conf import settings

from products.models import Product, ProductOption


class CartProductNotExist(Exception):
    def __init__(self, product_option, *args):
        super().__init__(*args)
        self.msg = f'{product_option.product.title} is not exist'

    def __str__(self):
        return self.msg


class CartProductOptionNotExist(Exception):
    def __init__(self, product_option, *args):
        super().__init__(*args)
        self.msg = f'{product_option.title} is not exist'

    def __str__(self):
        return self.msg


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.products = self.session.get(settings.CART_SESSION_ID, {})

        not_exist_pk_list = []
        for key in self.products:
            if not ProductOption.objects.values('pk').filter(pk=key).exists():
                not_exist_pk_list.append(key)
        for not_exist_pk in not_exist_pk_list:
            del self.products[not_exist_pk]

    def add(self, product_option, quantity):
        product_pk = str(product_option.product.pk)
        product_option_pk = str(product_option.pk)

        self.products.setdefault(
            product_pk, {}
        ).setdefault(
            product_option_pk, 0
        )
        self.products[product_pk][product_option_pk] += quantity
        self.save()

    def remove(self, product_option):
        product_pk = str(product_option.product.pk)
        product_option_pk = str(product_option.pk)

        if product_pk not in self.products:
            raise CartProductNotExist(product_option)

        if product_option_pk not in self.products[product_pk]:
            raise CartProductOptionNotExist(product_option)

        del self.products[product_pk][product_option_pk]
        self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.products
        self.session.modified = True

    @property
    def items(self):
        return [
            {
                'product': Product.objects.get(pk=product_pk),
                'options': [
                    {
                        'option': ProductOption.objects.get(pk=option_pk),
                        'quantity': quantity,
                    } for option_pk, quantity in options.items()
                ],
            } for product_pk, options in self.products.items()
        ]

    def __iter__(self):
        for item in self.items:
            yield item

    def __len__(self):
        return len(self.products)

    def get_item_price(self, product_pk, product_option_pk):
        quantity = self.products[product_pk][product_option_pk]
        return ProductOption.objects.prefetch().get(pk=product_option_pk).price_per_unit * quantity

    @property
    def amount(self):
        return sum([self.get_item_price(product_pk, product_option_pk)
                    for product_pk, options in self.products.items()
                    for product_option_pk in options])
