from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


User._meta.get_field('username').verbose_name = '아이디'
