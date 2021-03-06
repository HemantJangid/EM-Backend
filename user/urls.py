from django.conf.urls import url
from .views.v1.signup import SignupView
from .views.v1.address import UserAddressView
from .views.v1.email import SendEmailView
from .views.v1.profile import UserProfileView
from .views.v1.lead import LeadView
from .views.v1.partner import PartnerView
from .views.v1.community_user import CommunityUserView

urlpatterns = [
    url(r'^v1/user/signup$', SignupView.as_view()),
    url(r'^v1/user/address$', UserAddressView.as_view()),
    url(r'^v1/user/email$', SendEmailView.as_view()),
    url(r'^v1/user/profile$', UserProfileView.as_view()),
    url(r'^v1/user/lead$', LeadView.as_view()),
    url(r'^v1/user/partner$', PartnerView.as_view()),
    url(r'^v1/user/community$', CommunityUserView.as_view())

]
