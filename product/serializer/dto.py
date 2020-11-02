from rest_framework import serializers
from core.models import Product, ProductContent


class ProductDto(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('uuid', 'name', 'is_out_of_stock')


class ProductContentDto(serializers.ModelSerializer):
    class Meta:
        model = ProductContent
        fields = ('landing_page_content', 'info_page_content_1', 'video_page_video_link', 'stats_page_heading',
                  'stats_page_content', 'stats_page_metrics', 'features_page_heading_1', 'features_page_content_1',
                  'features_page_metrics_1', 'info_page_content_2', 'pricing_page_amount', 'pricing_page_emi')
