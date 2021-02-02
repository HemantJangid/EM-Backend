from django.conf.urls import url
from .views.v1.vehicle import ProductVehicleListView
from .views.v1.details import ProductDetailView
from .views.v1.cart import CartView, GetCartView
from .views.v1.order import OrderView, GetOrderView
from .views.v1.transaction import PayOrderRazorapyView
from .views.v1.warranty import WarrantyView
from .views.v1.insurance import InsuranceView
from .views.v1.dealer import DealerView
from .views.v1.test_ride import TestRideView
from .views.v1.accessory import ProductAccessoryListView


urlpatterns = [
    url(r'^v1/product/vehicle/list$', ProductVehicleListView.as_view()),
    url(r'^v1/product/accessory/list$', ProductAccessoryListView.as_view()),
    url(r'^v1/product/(?P<product_id>[\w\-]+)/detail$', ProductDetailView.as_view()),
    url(r'^v1/cart/(?P<product_id>[\w\-]+)$', CartView.as_view()),
    url(r'^v1/cart$', GetCartView.as_view()),
    url(r'^v1/order$', OrderView.as_view()),
    url(r'^v1/order/(?P<order_id>[\w\-]+)/detail$', GetOrderView.as_view()),
    url(r'^v1/order/razorpay/pay$', PayOrderRazorapyView.as_view()),
    url(r'^v1/warranty$', WarrantyView.as_view()),
    url(r'^v1/insurance$', InsuranceView.as_view()),
    url(r'^v1/dealer/list$', DealerView.as_view()),
    url(r'^v1/test-ride$', TestRideView.as_view()),
]
