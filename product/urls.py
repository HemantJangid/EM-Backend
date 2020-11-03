from django.conf.urls import url
from .views.v1.vehicle import ProductListView
from .views.v1.details import ProductDetailView
from .views.v1.cart import CartView, GetCartView
from .views.v1.order import OrderView, GetOrderView

urlpatterns = [
    url(r'^v1/product/vehicle/list$', ProductListView.as_view()),
    url(r'^v1/product/(?P<product_id>[\w\-]+)/detail$', ProductDetailView.as_view()),
    url(r'^v1/cart/(?P<product_id>[\w\-]+)$', CartView.as_view()),
    url(r'^v1/cart$', GetCartView.as_view()),
    url(r'^v1/order$', OrderView.as_view()),
    url(r'^v1/order/(?P<order_id>[\w\-]+)/detail$', GetOrderView.as_view()),
]
