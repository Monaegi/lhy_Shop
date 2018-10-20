from django import forms
from django.contrib.auth import login, authenticate

from .models import User

__all__ = (
    'LoginForm',
    'SignupForm',
)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def login(self, request):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return user
        raise forms.ValidationError('아이디 또는 비밀번호가 잘못되었습니다')


def make_options(**kwargs):
    ret = {'class': 'form-control'}
    ret.update(**kwargs)
    return ret


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=make_options(placeholder='비밀번호'))
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=make_options(placeholder='비밀번호 확인'))
    )

    class Meta:
        model = User
        fields = (
            'username',
            'last_name',
            'first_name',
            'password1',
            'password2',
        )
        widgets = {
            'username': forms.TextInput(attrs=make_options(placeholder='아이디')),
            'last_name': forms.TextInput(attrs=make_options(placeholder='성')),
            'first_name': forms.TextInput(attrs=make_options(placeholder='이름')),
            'email': forms.EmailInput(attrs=make_options(placeholder='이메일')),
        }

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('비밀번호와 비밀번호확인란의 값이 다릅니다')
        return password2
