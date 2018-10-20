from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

from ..forms import LoginForm

__all__ = (
    'LoginView',
)


class LoginView(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            messages.success(request, '로그인 되었습니다')
        else:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다')
        return redirect(request.META['HTTP_REFERER'])
