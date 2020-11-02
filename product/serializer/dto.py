from rest_framework import serializers
from core.models import Product


class ProductDto(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('uuid', 'name', 'is_out_of_stock')
