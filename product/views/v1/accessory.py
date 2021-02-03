from rest_framework.views import APIView
from core.models import Product, PRODUCT_ACCESSORY, ProductInfo
from middleware.response import success
from product.serializer.dto import ProductDto, ProductInfoDto


class ProductAccessoryListView(APIView):
    def get(self, request):
        products = Product.objects.filter(is_archived=False).filter(type=PRODUCT_ACCESSORY).order_by('name').all()

        result = []
        for product in products:
            product_info = ProductInfo.objects.filter(product_id=product.id).first()
            if product_info:
                info_data = ProductInfoDto(product_info).data
            else:
                info_data = {}

            product_data = ProductDto(product).data
            product_data["info"] = info_data
            result.append(product_data)

        payload = {
            'products': result
        }
        return success(payload, 'products fetched successfully', True)
