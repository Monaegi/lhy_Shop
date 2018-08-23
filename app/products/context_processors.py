from .models import ProductCategory


def category(request):
    categories = ProductCategory.objects.filter(
        parent_category__isnull=True
    ).prefetch_related(
        'category_set'
    ).prefetch_related(
        'product_set'
    )
    context = {
        'categories': categories,
    }
    return context
