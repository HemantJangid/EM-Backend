from rest_framework import serializers


class OrderDao(serializers.Serializer):
    user_address_uuid = serializers.CharField(max_length=255)
    discount_code = serializers.CharField(max_length=255)


class PayOrdeRazorpayDao(serializers.Serializer):
    razorpay_id = serializers.CharField(max_length=255)
    order_id = serializers.CharField(max_length=255)


class AddCartDao(serializers.Serializer):
    quantity = serializers.IntegerField()
    color = serializers.CharField(max_length=255)


class WarrantyDao(serializers.Serializer):
    frame_number = serializers.CharField(max_length=255)
    purchase_date = serializers.DateField()
    dealer_or_online = serializers.CharField(max_length=255)
    
    
class PromocodeDao(serializers.Serializer):
    discount_code = serializers.CharField(max_length=255)


class InsuranceDao(serializers.Serializer):
    frame_number = serializers.CharField(max_length=255)


class TestRideBookingDao(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    organisation_name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    bike_name = serializers.CharField(max_length=255)
    dealer_id = serializers.IntegerField()
    preferred_date = serializers.DateField()
    preferred_time = serializers.TimeField()
