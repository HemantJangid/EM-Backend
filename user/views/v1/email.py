from rest_framework.views import APIView
from middleware.response import success, bad_request
from user.serializer.dao import SendEmailDao
from core.models import EmailLeadLogs
from util.email import send_mail


class SendEmailView(APIView):

    def post(self, request):
        attributes = SendEmailDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        email_lead_logs = EmailLeadLogs(**attributes.data["meta"])
        email_lead_logs.subject = attributes.data["subject"]
        email_lead_logs.save()

        send_mail(attributes.data["email"].split(","), attributes.data["subject"], attributes.data["message"])

        return success({}, "email send successfully", True)
