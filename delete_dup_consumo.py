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

   billing = Billing.objects.all().filter(consumer__company__name='Cemar').order_by('consumer','reference','code_type')

   anterior = billing.first()

   deletar = []

   for i in billing[1:]:
      #print "ANTERIOR" + "\t" + str(anterior.reference) + "\t" + str(anterior.code_type) + "\t"+ str(anterior.billed)
      #print "ATUAL" + "\t" + str(i.reference) + "\t" + str(i.code_type) + "\t"+ str(i.billed)

      if anterior.consumer == i.consumer and anterior.reference == i.reference and anterior.code_type == i.code_type and anterior.billed == i.billed:
         print str(i.consumer) + "\t" + str(i.reference) + "\t" + str(i.code_type)

         deletar.append(anterior.id)

      anterior = i

   for i in deletar:
      objeto = Billing.objects.get(id=i)
      objeto.delete()

# alterar read por billed caso o read seja maior que o billed

#   for i in billing:
#      if i.read > i.billed:
#         dump = i.billed
#         i.billed = i.read
#         i.read = dump
#         i.save()
