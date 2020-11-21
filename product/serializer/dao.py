from rest_framework import serializers


class OrderDao(serializers.Serializer):
    user_address_uuid = serializers.CharField(max_length=255)


class PayOrdeRazorpayDao(serializers.Serializer):
    razorpay_id = serializers.CharField(max_length=255)
    order_id = serializers.CharField(max_length=255)


class AddCartDao(serializers.Serializer):
    quantity = serializers.IntegerField()


class WarrantyDao(serializers.Serializer):
    frame_number = serializers.CharField(max_length=255)
