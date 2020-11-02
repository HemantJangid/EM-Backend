import uuid
from django.db import models

# Create your models here.

PRODUCT_VEHICLE = 'VEHICLE'
PRODUCT_ACCESSORY = 'ACCESSORY'


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
