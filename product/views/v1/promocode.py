from rest_framework.views import APIView
from core.models import Promocode
from middleware.response import success, bad_request
from middleware.request import auth_required
from product.serializer.dao import PromocodeDao
from product.serializer.dto import PromocodeDto


class ApplyPromocodeView(APIView):

    def post(self, request):
        attributes = PromocodeDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        promocode = Promocode.objects.filter(
            discount_code=attributes.data['discount_code']).first()
        if not promocode:
            return success({}, "invalid promocode", False)

        return success(PromocodeDto(promocode).data, "Promocode Applied", True)

