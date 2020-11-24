from rest_framework.views import APIView
from core.models import Lead
from middleware.response import success, bad_request
from user.serializer.dao import LeadDao


class LeadView(APIView):

    def post(self, request):
        attributes = LeadDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        meta = attributes.data["meta"]
        meta_list = []
        for key in meta:
            meta_list.append(key + " - " + str(meta[key]))
        meta_string = "\n".join(meta_list)

        data = {}
        data.update(attributes.data)
        data["meta"] = meta_string

        Lead.objects.create(**data)

        return success({}, "email send successfully", True)
