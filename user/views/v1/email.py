from rest_framework.views import APIView
from middleware.response import success, bad_request
from user.serializer.dao import SendEmailDao
from util.email import send_mail


class SendEmailView(APIView):

    def post(self, request):
        attributes = SendEmailDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        send_mail(attributes.data["email"], attributes.data["subject"], attributes.data["message"])

        return success({}, "email send successfully", True)
