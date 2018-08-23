from django.contrib import admin

from .product import *
from .product_category import *
from .product_option import *
from ..models import *

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductOption, ProductOptionAdmin)
admin.site.register(ProductOptionPrice)
admin.site.register(ProductOptionUnit)
