from rest_framework import serializers
from core.models import Product, ProductContent, Cart, Order, OrderItem


class ProductDto(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('uuid', 'name', 'is_out_of_stock', 'selling_price')


class ProductContentDto(serializers.ModelSerializer):
    class Meta:
        model = ProductContent
        fields = ('landing_page_content', 'info_page_content_1', 'video_page_video_link', 'stats_page_heading',
                  'stats_page_content', 'stats_page_metrics', 'features_page_heading_1', 'features_page_content_1',
                  'features_page_metrics_1', 'info_page_content_2', 'pricing_page_amount', 'pricing_page_emi',
                  'features_page_heading_2')


class CartDto(serializers.ModelSerializer):
    product = ProductDto()

    class Meta:
        model = Cart
        fields = ('quantity', 'product')


class OrderItemDto(serializers.ModelSerializer):
    product = ProductDto()

    class Meta:
        model = OrderItem
        fields = ('quantity', 'product', 'amount')


class OrderDto(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('order_items', 'base_amount', 'id', 'total_amount', 'status')

    def get_order_items(self, obj):
        order_items = OrderItem.objects.filter(order=obj).all()
        return OrderItemDto(order_items, many=True).data
