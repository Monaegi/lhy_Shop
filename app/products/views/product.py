from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from ..models import Product, ProductCategory


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product_list.html'

    def get_queryset(self):
        category_pk = self.request.GET.get('category')
        if category_pk:
            category = get_object_or_404(ProductCategory, pk=category_pk)
            return super().get_queryset().filter(category=category)
        return super().get_queryset()


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'
    queryset = Product.objects.prefetch_related(
        'option_set__unit_set',
        'option_set__price_set',
    )
