from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

__all__ = (
    'LogoutView',
)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')
