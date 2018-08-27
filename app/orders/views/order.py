from django.views import View
from django.views.generic import DetailView

from ..models import Order

__all__ = (
    'OrderCompleteView',
)


class OrderCompleteView(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/order_complete.html'
