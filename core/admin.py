import requests
from emotorad.settings import WEBHOOK
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Product, ProductContent, Order, OrderItem, Transaction, Warranty, Lead, Partner, EmailLeadLogs, Dealer, \
    TestRideBooking, ProductInfo, Blog
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from csvexport.actions import csvexport


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)

    def save_model(self, request, obj, form, change):
        call_webhook()
        return super(ProductAdmin, self).save_model(request, obj, form, change)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


@admin.register(EmailLeadLogs)
class EmailLeadLogsAdmin(admin.ModelAdmin):
    search_fields = ['email', 'subject', 'form_name', 'name',
                     'address', 'phone', 'product_id', 'cycle_id', 'product_name']
    list_display = ('email', 'name', 'address', 'phone', 'form_name')
    actions = [csvexport]

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TestRideBooking)
class TestRideBookingAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'city',
                     'phone_number', 'preferred_date', 'dealer__name']
    list_display = ('name', 'phone_number', 'preferred_date',
                    'preferred_time', 'dealer')
    actions = [csvexport]

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ProductContent)
class ProductContentAdmin(admin.ModelAdmin, DynamicArrayMixin):

    def save_model(self, request, obj, form, change):
        call_webhook()
        return super(ProductContentAdmin, self).save_model(request, obj, form, change)


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin, DynamicArrayMixin):

    def save_model(self, request, obj, form, change):
        call_webhook()
        return super(ProductInfoAdmin, self).save_model(request, obj, form, change)


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
    list_display = ('transaction_id', 'medium', 'order_details')

    def order_details(self, obj):
        link = reverse("admin:core_order_change", args=[obj.order.id])
        return format_html('<a href="{0}">{1}</a>'.format(link, obj.order_id))
    order_details.allow_tags = True

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'frame_number', 'user',
                       'purchase_date', 'dealer_or_online')


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    search_fields = ['first_name']
    list_display = ('first_name', 'last_name', 'phone',
                    'email', 'address', 'query')

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'organisation_name', 'address',
                    'email', 'phone', 'interested_in')

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone_number']
    list_display = ('name', 'phone_number', 'address', 'is_active')

    def save_model(self, request, obj, form, change):
        call_webhook()
        return super(DealerAdmin, self).save_model(request, obj, form, change)


def call_webhook():
    url = WEBHOOK
    payload = "{}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.status_code)
