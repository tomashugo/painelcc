from __future__ import unicode_literals

from django.db import models
from mm.models import Company

# Create your models here.

class Type(models.Model):
   type = models.CharField(max_length=20)

   class Meta:
      verbose_name = "Tipo"

   def __str__(self):
      return self.type


class Sheet(models.Model):
   company = models.ForeignKey(Company)
   type = models.ForeignKey(Type)
   path = models.CharField(max_length=100)
   processed = models.BooleanField()
   date_time_processed = models.DateTimeField()
   
    