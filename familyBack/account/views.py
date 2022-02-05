from urllib import response
from account import models as accountModel
from rest_framework.views import APIView
from rest_framework.response import Response
from account import serializers as accountSerializer

from core import utils as coreUtils

class SignUp(APIView):
    def post(self, request):
        serializer = accountSerializer.SignUp(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        else:
            serializerInstance = serializer.data

        accountInstance = accountModel.Account.objects.create(
            firstName = serializerInstance.get("firstName"),
            lastName = serializerInstance.get("lastName"),
            dateOfBirth = coreUtils.strToDateTime(serializerInstance.get("dateOfBirth")),
            email = serializerInstance.get("email"),
            phone = serializerInstance.get("phone"),
        )
        accountInstance.save()

        return Response({"status":200})