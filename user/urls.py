from django.conf.urls import url
from .views.v1.signup import SignupView


urlpatterns = [
    url(r'^v1/user/signup$', SignupView.as_view())
]
