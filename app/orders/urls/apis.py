from django.urls import path

from ..apis import CartAPIView

urlpatterns = [
    path('cart/', CartAPIView.as_view()),
]
