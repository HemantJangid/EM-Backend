import requests
from emotorad.settings import WEBHOOK
from django.contrib import admin
from .models import Product, ProductContent, Order, OrderItem, Transaction, Warranty
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)

    def save_model(self, request, obj, form, change):
        call_webhook()
        return super(ProductAdmin, self).save_model(request, obj, form, change)


@admin.register(ProductContent)
class ProducContentAdmin(admin.ModelAdmin, DynamicArrayMixin):

    def save_model(self, request, obj, form, change):
        call_webhook()
        return super(ProducContentAdmin, self).save_model(request, obj, form, change)


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


def call_webhook():
    url = WEBHOOK
    payload = "{}"
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.status_code)
