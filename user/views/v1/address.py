from rest_framework.views import APIView
from core.models import UserAddress
from middleware.response import success, bad_request
from middleware.request import auth_required
from user.serializer.dao import AddAddressDao
from user.serializer.dto import UserAddressDto


class UserAddressView(APIView):

    @auth_required()
    def get(self, request):
        user_address_list = UserAddress.objects.filter(user=request.user, is_deleted=False).all()
        return success({"address_list": UserAddressDto(user_address_list, many=True).data}, "address fetched", True)

    @auth_required()
    def post(self, request):
        attributes = AddAddressDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        address = UserAddress(**attributes.data)
        address.user = request.user
        address.save()

        return success({}, "address saved successfully", True)
