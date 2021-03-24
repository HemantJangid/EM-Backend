from rest_framework.views import APIView
from core.models import OrderItem, Cart, Order, UserAddress
from middleware.response import success, bad_request
from middleware.request import auth_required
from product.serializer.dao import OrderDao
from product.serializer.dto import OrderDto


class OrderView(APIView):

    @auth_required()
    def post(self, request):
        attributes = OrderDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        user_address = UserAddress.objects.filter(
            user=request.user, uuid=attributes.data['user_address_uuid']).first()
        if not user_address:
            return success({}, "invalid user address", False)

        cart = Cart.objects.filter(user=request.user).all()
        if not cart:
            return success({}, "cannot create empty order", False)

        total_amount = 0
        for item in cart:
            total_amount += (item.product.selling_price * item.quantity)

        order = Order(total_amount=total_amount*100, user=request.user,
                      user_address=user_address, base_amount=total_amount*100)
        order.save()

        order_items = []
        for item in cart:
            product = item.product
            order_items.append(OrderItem(order=order,
                                         product=product,
                                         amount=product.selling_price,
                                         quantity=item.quantity))
        OrderItem.objects.bulk_create(order_items)

        for item in cart:
            item.delete()

        return success(OrderDto(order).data, "order created successfully", True)


class GetOrderView(APIView):

    @auth_required()
    def get(self, request, order_id):
        order = Order.objects.filter(user=request.user, id=order_id).first()
        if not order:
            return success({}, "invalid order id", False)

        return success(OrderDto(order).data, "order fetched successfully", True)
