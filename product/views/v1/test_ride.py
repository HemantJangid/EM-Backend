import datetime
import calendar
from rest_framework.views import APIView
from middleware.response import success, bad_request
from core.models import TestRideBooking, Dealer
from product.serializer.dao import TestRideBookingDao
from util.template import get_booking_confirmation_template, booking_reminder_template
from util.email import send_mail
from emotorad.settings import SERVER


class TestRideView(APIView):

    def post(self, request):
        attributes = TestRideBookingDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        dealer = Dealer.objects.filter(id=attributes.data["dealer_id"])

        booking_id = TestRideBooking.objects.create(**attributes.data).id
        booking = TestRideBooking.objects.filter(id=booking_id).first()

        message = get_booking_confirmation_template()
        send_mail(attributes.data["email"], "Booking Confirmation", message)

        if SERVER == "production":
            email_list = ["info@emotorad.com", "tech@emotorad.com"]
        else:
            email_list = []

        # send_mail(email_list, "Booking Confirmation", message)

        now = datetime.datetime.utcnow() + datetime.timedelta(seconds=19800)
        booking_dt_local = datetime.datetime.combine(booking.preferred_date, booking.preferred_time)
        diff = booking_dt_local - now
        total_seconds = diff.total_seconds()

        if booking_dt_local.date() == now.date() and total_seconds > 2 * 60 * 60:
            send_at = booking_dt_local - datetime.timedelta(seconds=19800) - datetime.timedelta(hours=2)
            reminder_template = booking_reminder_template()
            send_at_timestamp = calendar.timegm(send_at.timetuple())
            send_mail(attributes.data["email"], "Reminder", reminder_template, send_at=send_at_timestamp)

            booking.is_scheduled = True
            booking.scheduled_at = datetime.datetime.utcnow()
            booking.save()

        return success({}, "test ride booking successfull", True)
