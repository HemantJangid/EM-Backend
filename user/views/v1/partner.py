from rest_framework.views import APIView
from core.models import Partner
from middleware.response import success, bad_request
from user.serializer.dao import PartnerDao


class PartnerView(APIView):

    def post(self, request):
        attributes = PartnerDao(data=request.data)
        print("attributes: ", attributes)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        data = {}
        data.update(attributes.data)

        Partner.objects.create(**data)

        return success({}, "email send successfully", True)
