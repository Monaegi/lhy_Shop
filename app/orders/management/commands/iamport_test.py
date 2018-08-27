from django.conf import settings
from django.core.management import BaseCommand
from iamport import Iamport


class Command(BaseCommand):
    def handle(self, *args, **options):
        iamport = Iamport(imp_key=settings.IAMPORT_API_KEY, imp_secret=settings.IAMPORT_API_SECRET)
        iamport.find()
