from openpyxl import load_workbook
from django.core.wsgi import get_wsgi_application

import os
import sys

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from crews.models import Region
   from mm.models import Consumer, Meter, MeterHistory, Company
   from analysis.models import Billing, Register
   from datetime import datetime
   from django.shortcuts import get_object_or_404
   from adm.models import Type, Sheet

   celpa = Company.objects.get(name='Cemar')

   billings = Billing.objects.all().filter(consumer__company=celpa).order_by('consumer','reference','code_type')

   anterior = billings.first()

   deletar = []

   for i in billings:
      if i != billings.first():
         #print str(i.consumer.installation) + " " + str(i.reference) + " " + str(i.code_type)
         if (i.consumer == anterior.consumer) and (i.reference == anterior.reference) and (i.revenue_days == anterior.revenue_days) and (i.reader_msg == anterior.reader_msg) and (i.code_type == anterior.code_type) and (i.read == anterior.read) and (i.billed == anterior.billed) and (i.init_cycle == anterior.init_cycle) and (i.end_cycle == anterior.end_cycle):
            anterior.delete()
            #if i.consumer.installation == '106081930':
            #   print "lojas avenida"

      anterior = i
