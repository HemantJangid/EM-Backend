from rest_framework.views import APIView
from core.models import User
from middleware.response import success, bad_request
from middleware.request import auth_required
from user.serializer.dao import UserProfileDao


class UserProfileView(APIView):

    @auth_required()
    def post(self, request):
        attributes = UserProfileDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        User.objects.filter(id=request.user.id).update(
            phone_number=attributes.data["phone_number"],
            email=attributes.data["email"],
            name=str(attributes.data["first_name"] + " " + attributes.data["last_name"]).strip())

        return success({}, "profile updated successfully", True)
