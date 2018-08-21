from django.shortcuts import get_object_or_404

from .models import ProductCategoryTop, ProductCategoryMiddle, ProductCategorySmall


def categories(request):
    context = {
        'categories': ProductCategoryTop.objects.prefetch_related('sub_categories__sub_categories')
    }
    middle_category_pk = request.GET.get('middle_category')
    if middle_category_pk:
        middle_category = get_object_or_404(ProductCategoryMiddle, pk=middle_category_pk)
        context['cur_middle_category'] = middle_category
        context['cur_top_category'] = middle_category.top_category

    small_category_pk = request.GET.get('small_category')
    if small_category_pk:
        small_category = get_object_or_404(ProductCategorySmall, pk=small_category_pk)
        context['cur_small_category'] = small_category
    return context
