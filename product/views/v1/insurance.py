from rest_framework.views import APIView
from emotorad.settings import SERVER
from middleware.response import success, bad_request
from middleware.request import auth_required
from product.serializer.dao import InsuranceDao
from util.email import send_mail


class InsuranceView(APIView):

    @auth_required()
    def post(self, request):
        attributes = InsuranceDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        if SERVER == "production":
            email = "info@emotorad.com"
        else:
            email = "rajatvijay5@gmail.com"

        send_mail(email, "Insurance Request - " + attributes.data["frame_number"], attributes.data["frame_number"])

        return success({}, "insurance updated successfully", True)
