from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

__all__ = (
    'IamportCompleteView',
    'IamportTestView',
)


class IamportCompleteView(View):
    def get(self, request):
        return HttpResponse(str(request.GET))


class IamportTestView(TemplateView):
    template_name = 'orders/iamport_test.html'
