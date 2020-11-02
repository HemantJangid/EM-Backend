from rest_framework import serializers


class OrderDao(serializers.Serializer):
    user_address_uuid = serializers.CharField(max_length=255)
