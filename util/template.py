import datetime
from core.models import ProductContent


def get_booking_confirmation_template_customer(booking):
    from django.template.loader import render_to_string
    booking_dt_local = datetime.datetime.combine(
        booking.preferred_date, booking.preferred_time)
    context = {
        "booking": booking,
        "booking_date": booking_dt_local.strftime("%d %B, %Y"),
        "booking_time": booking_dt_local.strftime("%I:%M%p"),
        "bike_name": booking.bike_name,
        "map_link": "https://www.google.com/maps/search/?api=1&query={0},{1}".format(booking.dealer.latitude, booking.dealer.longitude)
    }
    template = render_to_string(
        'test_ride_booking_customer.html', context=context)

    return template
    # booking_dt_local = datetime.datetime.combine(booking.preferred_date, booking.preferred_time)
    # template = """
    #     Hi {0}<br><br>
    #     Thanks for choosing Emotorad.<br><br>
    #     Your booking for {1} at {2} is confirmed. Here are the booking details:<br><br>
    #     <b>Store Name</b>: {3}<br>
    #     <b>Store Address</b>: {4}<br>
    #     <b>Store Location</b>: {5}<br>
    #     <b>Booking Date</b>: {6}<br>
    #     <b>Booking Time</b>: {7}<br><br><br>
    #     In case of any queries, please reach out to us at info@emotorad.com
    # """.format(booking.name, booking.product.name, booking_dt_local.strftime("%d %B, %Y  %I:%M%p"),
    #            booking.dealer.name, booking.dealer.address,
    #            "https://www.google.com/maps/search/?api=1&query={0},{1}".format(booking.dealer.latitude, booking.dealer.longitude),
    #            booking_dt_local.strftime("%d %B, %Y"), booking_dt_local.strftime("%I:%M%p"))
    # return template


def get_booking_confirmation_template_dealer(booking):
    booking_dt_local = datetime.datetime.combine(
        booking.preferred_date, booking.preferred_time)
    template = """
        Hi {0}<br><br>
        You have a test ride booking for {1} at {2} is confirmed. Here are the booking details:<br><br>
        <b>Customer Name</b>: {3}<br>
        <b>Customer Mobile</b>: {4}<br>
        <b>Customer Email</b>: {5}<br>
        <b>Booking Date</b>: {6}<br>
        <b>Booking Time</b>: {7}<br><br><br>
        In case of any queries, please reach out to us at info@emotorad.com
    """.format(booking.dealer.name, booking.bike_name, booking_dt_local.strftime("%d %B, %Y  %I:%M%p"),
               booking.name, booking.phone_number, booking.email,
               booking_dt_local.strftime("%d %B, %Y"), booking_dt_local.strftime("%I:%M%p"))
    return template


def booking_reminder_template(booking):
    booking_dt_local = datetime.datetime.combine(
        booking.preferred_date, booking.preferred_time)
    template = """
        Hi {0}<br><br>
        Thanks for choosing Emotorad.<br><br>
        This is a reminder email in reference to your booking for {1} at {2} is confirmed. Here are the booking details:<br><br>
        <b>Store Name</b>: {3}<br>
        <b>Store Address</b>: {4}<br>
        <b>Store Location</b>: {5}<br>
        <b>Booking Date</b>: {6}<br>
        <b>Booking Time</b>: {7}<br><br><br>
        In case of any queries, please reach out to us at info@emotorad.com
    """.format(booking.name, booking.product.name, booking_dt_local.strftime("%d %B, %Y  %I:%M%p"),
               booking.dealer.name, booking.dealer.address,
               "https://www.google.com/maps/search/?api=1&query={0},{1}".format(
                   booking.dealer.latitude, booking.dealer.longitude),
               booking_dt_local.strftime("%d %B, %Y"), booking_dt_local.strftime("%I:%M%p"))
    return template
