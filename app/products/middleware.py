from django.utils.deprecation import MiddlewareMixin


class ProductCategoryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass
