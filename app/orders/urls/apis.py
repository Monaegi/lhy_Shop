from django.urls import path

from ..apis import CartAPIView

app_name = 'orders'
urlpatterns = [
    path('cart/', CartAPIView.as_view(), name='cart'),
]
