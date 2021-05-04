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

        warranty = Warranty.objects.filter(
            frame_number=attributes.data["frame_number"]).first()

        if warranty:
            return success({}, "warranty already claimed", False)

        print(attributes.data)
        warranty = Warranty.objects.create(user=request.user,
                                           name=attributes.data["name"],
                                           phone=attributes.data["phone"],
                                           frame_number=attributes.data["frame_number"],
                                           purchase_date=attributes.data["purchase_date"],
                                           dealer_or_platform=attributes.data["dealer_or_platform"],
                                           dealer_or_online=attributes.data["dealer_or_online"])
        warranty.save()

        return success({}, "warranty updated successfully", True)
