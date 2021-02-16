from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import User, Cart, UserAddress, Order, OrderItem, EmailLeadLogs, Dealer, TestRideBooking


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print("hello")
        # for booking in TestRideBooking.objects.using("master").all():
        #     dealer = Dealer.objects.filter(name=booking.dealer.name).first()
        #     if not dealer:
        #         continue
        #     print(booking.id)
        #     booking.pk = None
        #     booking.dealer_id = dealer.id
        #     booking.save()


# users = User.objects.all()
# for user in users:
#     if user.email:
#         temp = User.objects.using("master").filter(id=user.id).first()
#         if temp:
#             print("user found ignoring")
#             continue
#
#     print(user.id)
#
#     user.save(using="master")
#     carts = Cart.objects.filter(user_id=user.id)
#     for cart in carts:
#         cart.pk = None
#         cart.save(using="master")
#
#     address_list = UserAddress.objects.filter(user_id=user.id)
#     address_map = {}
#     for address in address_list:
#         current_id = address.id
#         address.pk = None
#         address.save(using="master")
#         address_map[current_id] = address.id
#
#     orders = Order.objects.filter(user_id=user.id)
#     for order in orders:
#         order.user_address_id = address_map[order.user_address_id]
#         order.save(using="master")
#
#         for item in OrderItem.objects.filter(order_id=order.id):
#             item.pk = None
#             item.save(using="master")
