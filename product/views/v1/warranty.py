from rest_framework.views import APIView
from core.models import Warranty
from middleware.response import success, bad_request
from middleware.request import auth_required
from product.serializer.dao import WarrantyDao


class WarrantyView(APIView):

    @auth_required()
    def post(self, request):
        attributes = WarrantyDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        warranty = Warranty.objects.filter(frame_number=attributes.data["frame_number"]).first()
        if not warranty:
            return success({}, "invalid frame number", False)

        if warranty.user_id:
            return success({}, "warranty already claimed", False)

        warranty.user = request.user
        warranty.save()

        return success({}, "warranty updated successfully", True)
