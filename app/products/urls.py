from django.urls import path

from .views import (
    ProductCategoryMiddleListView,
)

app_name = 'products'
urlpatterns = [
    path('category/<int:top_category_pk>/',
         ProductCategoryMiddleListView.as_view(),
         name='category-middle-list'),
]
