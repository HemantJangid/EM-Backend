from rest_framework.views import APIView
from core.models import Order, ORDER_COMPLETED, ORDER_PROCESSING, Transaction
from middleware.response import success, bad_request
from middleware.request import auth_required
from product.serializer.dao import PayOrdeRazorpayDao


class PayOrderRazorapyView(APIView):

    @auth_required()
    def post(self, request):
        attributes = PayOrdeRazorpayDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        razorpay_id = attributes.data["razorpay_id"]
        order = Order.objects.filter(user=request.user, id=attributes.data["order_id"]).first()
        if not order:
            return success({}, "invalid order id", False)

        if order.status == ORDER_COMPLETED:
            return success({}, "order already completed", False)

        order.status = ORDER_PROCESSING
        order.save()

        transaction = Transaction(order=order, transaction_id=razorpay_id, medium='razorpay', amount=order.total_amount)
        transaction.save()

        order.status = ORDER_COMPLETED
        order.save()

        return success({}, "payment completed", True)