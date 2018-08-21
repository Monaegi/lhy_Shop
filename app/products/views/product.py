from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView

from ..models import (
    Product, ProductCategoryMiddle, ProductCategorySmall)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        qs = super().get_queryset()
        middle_category_pk = self.request.GET.get('middle_category')
        small_category_pk = self.request.GET.get('small_category')

        if not middle_category_pk:
            raise Http404()
        if small_category_pk:
            qs = qs.filter(category=small_category_pk)
        else:
            qs = qs.filter(category__middle_category=middle_category_pk)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        middle_category = ProductCategoryMiddle.objects.get(pk=self.request.GET.get('middle_category'))
        small_category_pk = self.request.GET.get('small_category')
        context['top_category'] = middle_category.top_category
        context['breadcrumbs'] = [
            {
                'title': 'Home',
                'href': reverse('index'),
            },
            {
                'title': middle_category.top_category.title,
                'href': reverse('products:category-middle-list', args=(middle_category.top_category.pk,)),
            },
            {
                'title': middle_category.title,
            },
        ]
        if small_category_pk:
            small_category = get_object_or_404(ProductCategorySmall, pk=small_category_pk)
            context['breadcrumbs'].pop()
            context['breadcrumbs'].insert(-1, {
                'title': small_category.title,
            })
        return context
