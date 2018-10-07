from django.shortcuts import render
from django.views import View


class SignupView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'members/signup.html', context)
