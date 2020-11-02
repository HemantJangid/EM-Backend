from rest_framework.views import APIView
from core.models import ProductContent, Product
from middleware.response import success
from product.serializer.dto import ProductContentDto


class ProductDetailView(APIView):
    def get(self, request, product_id):
        product = Product.objects.filter(uuid=product_id, is_archived=False).first()
        if not product:
            return success({}, "invalid product id", False)

        content = ProductContent.objects.filter(product=product).first()
        if not content:
            return success({}, "no content is present", False)

        return success(ProductContentDto(content).data, "details fetched successfully", True)
