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
   from mm.models import Consumer
   from analysis.models import Inspection
   from adm.models import Type, Sheet


   inspecao = Type.objects.get(type="Inspecao")

   planilhas = Sheet.objects.all().filter(type=inspecao)

   for p in planilhas:
      wb = load_workbook(filename=p.path)
      ws = wb['Exportar Planilha']
      print p.path
      x = 0

      for i in ws:
#         print x
         if x > 0:

            installation = str(int(i[0].value))
            nota_de_servico = i[1].value

            try:
               observation  = i[5].value
            except AttributeError:
               observation = "Nada"

	    if observation is None:
               observation = "Nada"


            inspection = Inspection.objects.all().filter(ns=nota_de_servico)
  
            if len(inspection) > 0:
	            inspection = inspection.first()
          	    inspection.observation = observation
  	            inspection.save()
      
         x = x + 1
