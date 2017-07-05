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
   from analysis.models import Billing, Register, RelatorioQuedaDeConsumo
   from datetime import datetime
   from django.shortcuts import get_object_or_404
   from adm.models import Type, Sheet

   empresa = Company.objects.get(name='Celpa')

   reports = RelatorioQuedaDeConsumo.objects.all().filter(company=empresa).order_by('consumer','referencia')

   anterior = reports.first()

   deletar = []

   for i in reports:
      if i != reports.first():
         if (i.consumer == anterior.consumer) and (i.referencia == anterior.referencia):
            anterior.delete()

      anterior = i
