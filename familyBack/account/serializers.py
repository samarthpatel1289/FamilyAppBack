import email
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from core import constants as coreConstants
from core import utils as coreUtils

class SignUp(serializers.Serializer):
    firstName = serializers.CharField(max_length=100)
    lastName = serializers.CharField(max_length=100)
    dateOfBirth = serializers.DateField(format=coreConstants.DATE_FORMAT, input_formats=[coreConstants.DATE_FORMAT , ])
    email = serializers.EmailField()
    phone = serializers.IntegerField()

    def validate_firstName(self, data):
        return data

    def validate_lastName(self, data):
        return data

    def validate_dateOfBirth(self, data):
        return data

    def validate_email(self, data):
        return data

    def validate_phone(self, data):
        if coreUtils.validate_phone(data):    
            return data
        else:
            raise serializers.ValidationError("Phone Number must be less than or equal to 10 in length")

    