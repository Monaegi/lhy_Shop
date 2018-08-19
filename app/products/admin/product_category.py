from django.contrib import admin

__all__ = (
    'ProductCategoryTopAdmin',
    'ProductCategoryMiddleAdmin',
    'ProductCategorySmallAdmin',
    'ProductCategoryAdmin',
)


class ProductCategoryTopAdmin(admin.ModelAdmin):
    pass


class ProductCategoryMiddleAdmin(admin.ModelAdmin):
    pass


class ProductCategorySmallAdmin(admin.ModelAdmin):
    pass


class ProductCategoryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/product_category_change_list.html'

    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(request, extra_context)
    #
    #     try:
    #         qs = response.context_data['cl'].queryset
    #     except (AttributeError, KeyError):
    #         return response
    #
    #