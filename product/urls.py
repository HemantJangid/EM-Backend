from django.conf.urls import url
from .views.v1.vehicle import ProductListView

urlpatterns = [
    url(r'^v1/product/vehicle/list$', ProductListView.as_view()),
]
