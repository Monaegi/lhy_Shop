from .cart import Cart


def cart(request):
    context = {
        'cart': Cart(request).products,
    }
    return context
