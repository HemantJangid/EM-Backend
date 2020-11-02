from rest_framework.views import APIView
from core.models import Product, Cart
from middleware.response import success
from middleware.request import auth_required
from product.serializer.dto import CartDto


class CartView(APIView):

    @auth_required()
    def post(self, request, product_id):
        product = Product.objects.filter(uuid=product_id, is_archived=False).first()
        if not product:
            return success({}, "invalid product id", False)

        if product.is_out_of_stock:
            return success({}, "product out of stock", False)

        cart = Cart.objects.filter(product=product, user=request.user).first()
        if not cart:
            cart = Cart(product=product, user=request.user)
        else:
            cart.quantity += 1
        cart.save()

        return success({}, "product added successfully", True)

    @auth_required()
    def delete(self, request, product_id):
        product = Product.objects.filter(uuid=product_id, is_archived=False).first()
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
