from rest_framework.views import APIView
from core.models import Product, Cart
from middleware.response import success, bad_request
from middleware.request import auth_required
from product.serializer.dao import AddCartDao
from product.serializer.dto import CartDto


class CartView(APIView):

    @auth_required()
    def post(self, request, product_id):
        attributes = AddCartDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        product = Product.objects.filter(
            uuid=product_id, is_archived=False).first()
        if not product:
            return success({}, "invalid product id", False)

        cart = Cart.objects.filter(product=product, user=request.user).first()
        if not cart:
            cart = Cart(product=product, user=request.user)
            cart.quantity = attributes.data["quantity"]
        else:
            cart.quantity += attributes.data["quantity"]
        cart.save()

        return success({}, "product added successfully", True)

    @auth_required()
    def delete(self, request, product_id):
        product = Product.objects.filter(
            uuid=product_id, is_archived=False).first()
        if not product:
            return success({}, "invalid product id", False)

        cart = Cart.objects.filter(product=product, user=request.user).first()
        if not cart:
            return success({}, "product not present in cart", False)

        if cart.quantity == 1:
            cart.delete()
        else:
            cart.quantity -= 1
            cart.save()

        return success({}, "product removed successfully", True)


class GetCartView(APIView):

    @auth_required()
    def get(self, request):
        carts = Cart.objects.filter(user=request.user).all()
        return success({"products": CartDto(carts, many=True).data}, "product removed successfully", True)
