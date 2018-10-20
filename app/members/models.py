from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @property
    def name(self):
        return '{last}{first}'.format(
            last=self.last_name,
            first=self.first_name,
        )


User._meta.get_field('username').verbose_name = '아이디'
