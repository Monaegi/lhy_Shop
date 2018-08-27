from django.urls import path

from ..views import *

app_name = 'orders'
urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('payments/complete/', IamportCompleteView.as_view(), name='iamport-complete'),

    path('iamport/test/', IamportTestView.as_view(), name='iamport-test'),
]
