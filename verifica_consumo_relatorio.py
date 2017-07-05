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
   from analysis.models import Inspection, Billing, RelatorioQuedaDeConsumo
   from adm.models import Type, Sheet

   billing = Billing.objects.all().order_by('consumer','reference','code_type')

   anterior = billing.first()

   for i in billing[1:]:
      if anterior.consumer == i.consumer and anterior.reference == i.reference and anterior.code_type == i.code_type:
         queda_consumo = RelatorioQuedaDeConsumo.objects.all().filter(referencia__gte=i.reference).filter(consumer=i.consumer)
         if len(queda_consumo) > 0:
            print i.consumer


