from django.contrib import admin
from .models import Product, ProductContent, Order, OrderItem
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductContent)
class ProducContentAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['status']

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ['order__id']

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
