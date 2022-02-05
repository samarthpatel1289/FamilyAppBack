from django.db import models

class BaseModel(models.Model):
    isdelete = models.BooleanField(default=False)