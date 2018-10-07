from .forms import SignupForm


def form(request):
    return {
        'signup_form': SignupForm(),
    }
