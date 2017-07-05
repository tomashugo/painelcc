# -*- coding: utf-8 -*-
from openpyxl import load_workbook
from django.core.wsgi import get_wsgi_application

import os
import sys
import datetime

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from crews.models import Region
   from mm.models import Consumer, Company
   from analysis.models import Inspection, Billing
   from adm.models import Type, Sheet

   billing = Billing.objects.all().filter(consumer__company__name = 'Cemar')
   
   for i in billing:
      if i.read > i.billed:
         dumb = i.read
         i.read = i.billed
         i.billed = dumb
         i.save()

         print "Lido maior que faturado\t" + str(i.consumer) + "\t" + str(i.reference) + "\t" + str(i.read) + "\t" + str(i.billed)