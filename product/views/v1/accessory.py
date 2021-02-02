from rest_framework.views import APIView
from core.models import Product, PRODUCT_ACCESSORY
from middleware.response import success
from product.serializer.dto import ProductDto


class ProductAccessoryListView(APIView):
    def get(self, request):
        products = Product.objects.filter(is_archived=False).filter(type=PRODUCT_ACCESSORY).order_by('name').all()
        payload = {
            'products': ProductDto(products, many=True).data
        }
        return success(payload, 'products fetched successfully', True)
