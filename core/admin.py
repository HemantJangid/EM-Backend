from django.contrib import admin
from .models import Product, ProductContent
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductContent)
class ProducContentAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass
