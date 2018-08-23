from django.contrib import admin
from ..forms import ProductOptionForm


class ProductOptionAdmin(admin.ModelAdmin):
    form = ProductOptionForm

    def get_changeform_initial_data(self, request):
        data = super().get_changeform_initial_data(request)
        print(data)
        return data

