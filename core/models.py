import uuid
import random
import string
from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField

PRODUCT_VEHICLE = 'VEHICLE'
PRODUCT_ACCESSORY = 'ACCESSORY'
ORDER_VIRTUAL = 'VIRTUAL'


def get_default_json():
    return {}


def get_default_list():
    return []


class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True, default='')
    email = models.CharField(max_length=255, null=True, blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return str(self.id)


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
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    landing_page_content = models.TextField(null=True, blank=True)
    landing_page_image = models.CharField(max_length=255, null=True, blank=True, default='')
    info_page_content_1 = models.TextField(null=True, blank=True)
    info_page_content_2 = models.TextField(null=True, blank=True)
    video_page_video_link = models.CharField(max_length=255, null=True, blank=True, default='')
    stats_page_heading = models.TextField(null=True, blank=True)
    stats_page_content = models.TextField(null=True, blank=True)
    stats_page_metrics = models.JSONField(default=get_default_json, blank=True)
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


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cart'


class UserAddress(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=True, default='')
    phone_number = models.CharField(max_length=255, null=True, blank=True, default='')
    pincode = models.CharField(max_length=255, null=True, blank=True, default='')
    addless_line_1 = models.CharField(max_length=255, null=True, blank=True, default='')
    addless_line_2 = models.CharField(max_length=255, null=True, blank=True, default='')
    landmark = models.CharField(max_length=255, null=True, blank=True, default='')
    city = models.CharField(max_length=255, null=True, blank=True, default='')
    state = models.CharField(max_length=255, null=True, blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_address'


class Order(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, default=ORDER_VIRTUAL)
    base_amount = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)
    gst_amount = models.IntegerField(default=0)
    discount_amount = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        super(Order, self).save(*args, **kwargs)

    class Meta:
        db_table = 'order'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_item'


class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255)
    medium = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transaction'
