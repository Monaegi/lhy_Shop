from django.contrib import admin

__all__ = (
    'ProductCategoryTopAdmin',
    'ProductCategoryMiddleAdmin',
    'ProductCategorySmallAdmin',
)


class ProductCategoryTopAdmin(admin.ModelAdmin):
    pass


class ProductCategoryMiddleAdmin(admin.ModelAdmin):
    pass


class ProductCategorySmallAdmin(admin.ModelAdmin):
    pass
