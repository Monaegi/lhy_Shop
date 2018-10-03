from django.urls import path

from ..apis import CartAPIView, CartClearAPIView

app_name = 'orders'
urlpatterns = [
    path('cart/', CartAPIView.as_view(), name='cart'),
    path('cart/clear/', CartClearAPIView.as_view()),
]
