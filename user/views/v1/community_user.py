from rest_framework.views import APIView
from core.models import CommunityUser
from middleware.response import success, bad_request
from middleware.request import auth_required
from user.serializer.dao import CommunityUserDao 


class CommunityUserView(APIView):

    def post(self, request):
        attributes = CommunityUserDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        user = CommunityUser.objects.filter(
            frame_number=attributes.data["frame_number"]).first()

        if user:
            return success({}, "User Already exists for this frame number.", False)
        
        user = CommunityUser.objects.filter(email=attributes.data["email"]).first()

        if user:
            return success({}, "User Already exists for this email.", False)

        print(attributes.data)
        user = CommunityUser.objects.create(
                                           name=attributes.data["name"],
                                           phone=attributes.data["phone"],
                                           frame_number=attributes.data["frame_number"],
                                           email=attributes.data["email"],
                                           city=attributes.data["city"])
        user.save()

        return success({}, "User created successfully", True)
