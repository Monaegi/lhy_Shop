from django.db import models

__all__ = (
    'TimeStampedMixin',
    'TimeStampedModel',
)


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TimeStampedModel(TimeStampedMixin, models.Model):
    class Meta:
        abstract = True
