import datetime
import calendar
from core.models import TestRideBooking
from django.core.management.base import BaseCommand
from util.template import booking_reminder_template
from util.email import send_mail


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        now = datetime.datetime.utcnow() + datetime.timedelta(seconds=19800)
        print("Scheduling emails for day -> ", now.date())

        bookings = TestRideBooking.objects.filter(preferred_date=now.date(), is_scheduled=False)
        for booking in bookings:
            booking_dt_local = datetime.datetime.combine(booking.preferred_date, booking.preferred_time)
            send_at = booking_dt_local - datetime.timedelta(seconds=19800) - datetime.timedelta(hours=2)
            print("scheduling email for booking id", booking.id)

            reminder_template = booking_reminder_template()
            send_at_timestamp = calendar.timegm(send_at.timetuple())
            send_mail(booking.email, "Reminder", reminder_template, send_at=send_at_timestamp)

            booking.is_scheduled = True
            booking.scheduled_at = datetime.datetime.utcnow()
            booking.save()
