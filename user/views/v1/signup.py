from rest_framework.views import APIView
from core.models import User
from middleware.response import success, bad_request
from user.serializer.dao import SignupDao
from util.firebase_auth import get_firebase_user_data


class SignupView(APIView):

    def post(self, request):
        attributes = SignupDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        firebase_data = get_firebase_user_data(attributes.data["firebase_token"])
        if not firebase_data:
            return success({}, False, "invalid firesbase token")

        user_id = firebase_data["user_id"]
        user = User.objects.filter(id=user_id).first()
        if not user:
            user = User(id=user_id)
        user.save()

        return success({}, "signup completed", True)
