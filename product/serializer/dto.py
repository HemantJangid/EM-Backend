from rest_framework import serializers
from core.models import Product, ProductContent


class ProductDto(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('uuid', 'name', 'is_out_of_stock')


class ProductContentDto(serializers.ModelSerializer):
    class Meta:
        model = ProductContent
        fields = ('landing_page_content', 'info_page_content_1')
