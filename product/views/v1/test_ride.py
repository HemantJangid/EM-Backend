from rest_framework.views import APIView
from middleware.response import success, bad_request
from core.models import TestRideBooking
from product.serializer.dao import TestRideBookingDao


class TestRideView(APIView):

    def post(self, request):
        attributes = TestRideBookingDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        TestRideBooking.objects.create(**attributes.data)

        return success({}, "test ride booking successfull", True)
