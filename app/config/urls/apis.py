from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('orders/', include('orders.urls.apis')),
]
