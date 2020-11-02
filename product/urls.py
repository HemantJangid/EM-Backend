from django.conf.urls import url
from .views.v1.vehicle import ProductListView
from .views.v1.details import ProductDetailView

urlpatterns = [
    url(r'^v1/product/vehicle/list$', ProductListView.as_view()),
    url(r'^v1/product/detail$', ProductDetailView.as_view()),
]
