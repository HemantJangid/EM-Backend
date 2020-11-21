from django.contrib import admin
from .models import Product, ProductContent, Order, OrderItem, Transaction, Warranty
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


@admin.register(ProductContent)
class ProducContentAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['status', 'id']
    list_display = ('id', 'status')

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ['order__id', 'product__name']
    list_display = ('order', 'product', 'quantity')

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ['order__id']
    list_display = ('order', 'transaction_id', 'medium')

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'user')
