from rest_framework.views import APIView
from middleware.response import success
from product.serializer.dto import DealerDto
from core.models import Dealer


class DealerView(APIView):

    def get(self, request):
        dealers = Dealer.objects.filter(is_active=True)

        response = {
            "dealers": DealerDto(dealers, many=True).data
        }

        return success(response, "dealers fetched successfully", True)
