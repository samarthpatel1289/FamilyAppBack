#Django Imports
from django.db import models

#ThirdParty imports
import email
import uuid


#File Imports
from core import models as core_models
from core import constants as coreConstants


class Account(core_models.BaseModel):
    accountId = models.UUIDField(default=uuid.uuid4)
    firstName = models.TextField(max_length=100)
    lastName = models.TextField(max_length=100)
    dateOfBirth = models.DateField()
    phone = models.CharField(max_length=12)
    email = models.EmailField()

# Create your models here.
