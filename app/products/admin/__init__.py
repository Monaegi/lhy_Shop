from django.contrib import admin

from .product import *
from .product_category import *
from ..models import *

admin.site.register(ProductCategoryTop, ProductCategoryTopAdmin)
admin.site.register(ProductCategoryMiddle, ProductCategoryMiddleAdmin)
admin.site.register(ProductCategorySmall, ProductCategoryTopAdmin)
