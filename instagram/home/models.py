from logging import PlaceHolder
from django.db import models
import uuid

# Create your models here.

class Details(models.Model):
    research = models.CharField(max_length=200, blank=True, null=True)
    info = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add = True)


    # def __str__(self):
    #     return self.research
