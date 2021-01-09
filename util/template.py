

def get_booking_confirmation_template(booking):
    template = """
        <b>Booking Date</b>: {0}<br>
        <b>Booking Time</b>: {1}<br>
        <b>Dealer Name</b>: {2}<br>
        <b>Dealer Address</b>: {3}<br>
        <b>Dealer City</b>: {4}<br>
        <b>Product Name</b>: {5}<br>
    """.format(booking.preferred_date, booking.preferred_time,
               booking.dealer.name, booking.dealer.address, booking.dealer.city, booking.product.name)
    return template


def booking_reminder_template(booking):
    template = """
        <b>Booking Date</b>: {0}<br>
        <b>Booking Time</b>: {1}<br>
        <b>Dealer Name</b>: {2}<br>
        <b>Dealer Address</b>: {3}<br>
        <b>Dealer City</b>: {4}<br>
        <b>Product Name</b>: {5}<br>
    """.format(booking.preferred_date, booking.preferred_time,
               booking.dealer.name, booking.dealer.address, booking.dealer.city, booking.product.name)
    return template
