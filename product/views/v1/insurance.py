from rest_framework.views import APIView
from emotorad.settings import SERVER
from middleware.response import success, bad_request
from middleware.request import auth_required
from product.serializer.dao import InsuranceDao
from util.email import send_mail
from core.models import InsuranceRequest


class InsuranceView(APIView):

    def post(self, request):
        attributes = InsuranceDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        if SERVER == "production":
            email = "info@emotorad.com"
        else:
            email = "rajatvijay5@gmail.com"
            
        insurance = InsuranceRequest.objects.create(
                                           name=attributes.data["name"],
                                           phone=attributes.data["phone"],
                                           frame_number=attributes.data["frame_number"],
                                           purchase_date=attributes.data["purchase_date"],
                                           dealer_or_platform=attributes.data["dealer_or_platform"],
                                           dealer_or_online=attributes.data["dealer_or_online"])
        insurance.save()
        # message = """
        #     Frame Number -> {}<br>
        #     Customer Name -> {}<br>
        #     Customer Email -> {}<br>
        #     Customer Phone Number -> {}
        # """.format(attributes.data["frame_number"], request.user.name, request.user.email, request.user.phone_number)

        # send_mail(email, "Insurance Request - " + attributes.data["frame_number"], message)

        return success({}, "insurance updated successfully", True)
