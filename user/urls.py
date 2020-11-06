from django.conf.urls import url
from .views.v1.signup import SignupView
from .views.v1.address import UserAddressView


urlpatterns = [
    url(r'^v1/user/signup$', SignupView.as_view()),
    url(r'^v1/user/address$', UserAddressView.as_view()),
    url(r'^v1/user/address$', UserAddressView.as_view())
]
