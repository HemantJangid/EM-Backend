from rest_framework import serializers
from core.models import UserAddress


class UserAddressDto(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ('uuid', 'full_name', 'phone_number', 'pincode', 'address_line_1', 'address_line_2', 'landmark', 'city',
                  'state')
