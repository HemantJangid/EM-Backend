from django.contrib import admin
from .models import Product, ProductContent


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductContent)
class ProducContenttAdmin(admin.ModelAdmin):
    pass
