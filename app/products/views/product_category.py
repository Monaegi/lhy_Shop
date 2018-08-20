from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View

from ..models import (
    ProductCategoryTop,
)


class ProductCategoryMiddleListView(View):
    def get(self, request, top_category_pk):
        top_category = get_object_or_404(ProductCategoryTop, pk=top_category_pk)
        context = {
            'top_category': top_category,
            'breadcrumbs': [
                {
                    'title': 'Home',
                    'href': reverse('index'),
                },
                {
                    'title': top_category.title,
                },
            ]
        }
        return render(request, 'products/category/middle-list.html', context)
