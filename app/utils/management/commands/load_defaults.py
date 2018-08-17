import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from products.models import (
    ProductCategoryTop,
    ProductCategoryMiddle,
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        def set_categories(data_top_categories):
            """
            ProductCategory의 기본값들을 세팅
            :param data_top_categories: 
            :return: 
            """
            for data_top_category in data_top_categories:
                top_category, __ = ProductCategoryTop.objects.get_or_create(
                    title=data_top_category['title'])
                for data_middle_category in data_top_category['middleCategories']:
                    ProductCategoryMiddle.objects.get_or_create(
                        top_category=top_category,
                        title=data_middle_category['title'],
                    )

        data = json.load(open(os.path.join(settings.CONFIGS_DIR, 'defaults.json')))
        set_categories(data['topCategories'])
