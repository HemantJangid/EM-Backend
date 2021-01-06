import datetime
from core.models import TestRideBooking
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        now = datetime.datetime.utcnow() + datetime.timedelta(seconds=19800)

        bookings = TestRideBooking.objects.filter(preferred_date=now.date())
        for booking in bookings:
            booking_dt_local = datetime.datetime.combine(booking.preferred_date, booking.preferred_time)
            send_at = booking_dt_local - datetime.timedelta(seconds=19800) - datetime.timedelta(hours=2)
            print(send_at)
            print("scheduling email for booking id", booking.id)
