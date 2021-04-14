import uuid
from rest_framework.views import APIView
from core.models import ProductContent, Product
from middleware.response import success
from product.serializer.dto import ProductContentDto


class ProductDetailView(APIView):
    def get(self, request, product_id):
        query = {'is_archived': False}
        if is_valid_uuid(product_id):
            query["uuid"] = product_id
        else:
            query["slug"] = product_id
        product = Product.objects.filter(**query).first()
        if not product:
            return success({}, "invalid product id", False)

        print("product: ", product)

        content = ProductContent.objects.filter(product=product).first()
        if not content:
            return success({}, "no content is present", False)

        return success(ProductContentDto(content).data, "details fetched successfully", True)


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False
