from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    # def get(self, request, *args, **kwargs):
    #     print(request.session.get('abc'))
    #     request.session['abc'] = 'def'
    #     print(request.session)
    #     return super().get(request, *args, **kwargs)
