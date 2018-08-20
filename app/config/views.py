from django.views.generic import TemplateView
from products.models import ProductCategoryTop


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategoryTop.objects.prefetch_related('sub_categories')
        return context
