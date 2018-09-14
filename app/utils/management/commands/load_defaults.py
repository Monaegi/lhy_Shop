import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from products.models import (
    ProductCategoryTop,
    ProductCategoryMiddle,
    ProductCategorySmall,
    Product, ProductPriceInfo)


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
                    middle_category, __ = ProductCategoryMiddle.objects.get_or_create(
                        top_category=top_category,
                        title=data_middle_category['title'],
                    )
                    for data_small_category in data_middle_category.get('smallCategories', []):
                        small_category, __ = ProductCategorySmall.objects.get_or_create(
                            middle_category=middle_category,
                            _title=data_small_category['title'],
                        )
                        for data_product in data_small_category.get('products', []):
                            product, __ = Product.objects.get_or_create(
                                category=small_category,
                                title=data_product['title'],
                                unit=data_product['unit'],
                            )
                            procuct_price, __ = ProductPriceInfo.objects.get_or_create(
                                product=product,
                                price=data_product['price']
                            )

        data = json.load(open(os.path.join(settings.CONFIGS_DIR, 'defaults.json')))
        set_categories(data['topCategories'])
