from django.contrib import admin

__all__ = (
    'ProductCategoryAdmin',
)


class ProductCategoryAdmin(admin.ModelAdmin):
    pass
    # change_list_template = 'admin/product_category_change_list.html'

    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(request, extra_context)
    #
    #     try:
    #         qs = response.context_data['cl'].queryset
    #     except (AttributeError, KeyError):
    #         return response
    #
    #