from django.urls import path

from .views import (
    ProductCategoryMiddleListView,
    ProductListView,
)

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('category/<int:top_category_pk>/',
         ProductCategoryMiddleListView.as_view(),
         name='category-middle-list'),
]
