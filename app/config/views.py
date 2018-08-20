from django.views.generic import TemplateView
from products.models import ProductCategoryTop


class IndexView(TemplateView):
    template_name = 'index.html'

