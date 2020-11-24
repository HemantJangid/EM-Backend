from rest_framework import serializers


class SignupDao(serializers.Serializer):
    firebase_token = serializers.CharField()


class AddAddressDao(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=14)
    pincode = serializers.CharField(max_length=10)
    address_line_1 = serializers.CharField(max_length=255)
    address_line_2 = serializers.CharField(max_length=255, required=False, allow_blank=True)
    landmark = serializers.CharField(max_length=255, required=False, default='', allow_blank=True)
    city = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)


class DeleteAddressDao(serializers.Serializer):
    address_uuid = serializers.CharField(max_length=255)


class SendEmailDao(serializers.Serializer):
    email = serializers.CharField()
    subject = serializers.CharField()
    message = serializers.CharField()


class LeadDao(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    city = serializers.CharField(max_length=255, required=False, default='', allow_blank=True)
    form_name = serializers.CharField()
    meta = serializers.DictField(child=serializers.CharField(), allow_empty=True)


class UserProfileDao(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255, required=False, default='', allow_blank=True)
    email = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=14)
