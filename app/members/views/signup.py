from django.shortcuts import render
from django.views import View

__all__ = (
    'SignupView',
)


class SignupView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'members/signup.html', context)
