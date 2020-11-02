import uuid
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField

PRODUCT_VEHICLE = 'VEHICLE'
PRODUCT_ACCESSORY = 'ACCESSORY'


def get_default_json():
    return {}


def get_default_list():
    return []


class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255, null=False, blank=False, default='ACCESSORY',
                            choices=[(PRODUCT_ACCESSORY, PRODUCT_ACCESSORY), (PRODUCT_VEHICLE, PRODUCT_VEHICLE)])
    maximum_retail_price = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)
    is_out_of_stock = models.BooleanField(default=False)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return str(self.name)


class ProductContent(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, unique=True)
    landing_page_content = models.TextField(null=True, blank=True)
    landing_page_image = models.CharField(max_length=255, null=True, blank=True)
    info_page_content_1 = models.TextField(null=True, blank=True)
    info_page_content_2 = models.TextField(null=True, blank=True)
    video_page_video_link = models.CharField(max_length=255, null=True, blank=True)
    stats_page_heading = models.TextField(null=True, blank=True)
    stats_page_content = models.TextField(null=True, blank=True)
    stats_page_metrics = models.JSONField(default=get_default_json)
    features_page_heading_1 = models.TextField(null=True, blank=True)
    features_page_content_1 = models.TextField(null=True, blank=True)
    features_page_metrics_1 = ArrayField(models.CharField(max_length=255), default=get_default_list, blank=True)
    features_page_metrics_2 = ArrayField(models.CharField(max_length=255), default=get_default_list, blank=True)
    pricing_page_amount = models.CharField(max_length=255, null=True, blank=True, default='0')
    pricing_page_emi = models.CharField(max_length=255, null=True, blank=True, default='0')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_content'

    def __str__(self):
        return str(self.product.name)
