from rest_framework.views import APIView
from core.models import ProductContent
from middleware.response import success
from product.serializer.dto import ProductDto


class ProductDetailView(APIView):
    def get(self, request):
        products = ProductContent.objects.filter(pk=1).first()
        print(products.landing_page_image)
