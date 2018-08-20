from .models import ProductCategoryTop


def categories(request):
    return {
        'categories': ProductCategoryTop.objects.prefetch_related('sub_categories')
    }
