from rest_framework import serializers
from core.models import Product, ProductContent, Cart, Order, OrderItem, UserAddress


class ProductDto(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('uuid', 'name', 'is_out_of_stock', 'selling_price', 'model_number', 'image_url', 'slug', 'title',
                  'bg_image')


class ProductContentDto(serializers.ModelSerializer):
    class Meta:
        model = ProductContent
        fields = ('landing_page_content', 'info_page_content_1', 'video_page_video_link', 'stats_page_heading',
                  'stats_page_content', 'stats_page_metrics', 'features_page_heading_1', 'features_page_content_1',
                  'features_page_metrics_1', 'info_page_content_2', 'pricing_page_amount', 'pricing_page_emi',
                  'features_page_heading_2', 'landing_page_image', 'features_page_metrics_2', 'primary_color',
                  'info_page_bg_image_url', 'info_4_bg_image_1', 'info_4_bg_image_2', 'whats_more_bg_image',
                  'features_page_main_stat', 'stats_bg_image', 'whats_more_subtitle_text')


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


class UserAddressDto(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('uuid', 'full_name', 'phone_number', 'pincode', 'address_line_1', 'address_line_2', 'landmark', 'city',
                  'state')


class OrderDto(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    user_address = UserAddressDto()

    class Meta:
        model = Order
        fields = ('order_items', 'base_amount', 'id', 'total_amount', 'status', 'user_address')

    def get_order_items(self, obj):
        order_items = OrderItem.objects.filter(order=obj).all()
        return OrderItemDto(order_items, many=True).data
