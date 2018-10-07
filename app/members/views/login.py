from django.contrib.auth.views import LoginView as DjangoLoginView

__all__ = (
    'LoginView',
)


class LoginView(DjangoLoginView):
    pass
