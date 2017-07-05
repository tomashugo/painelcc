from openpyxl import load_workbook
from django.core.wsgi import get_wsgi_application

import os
import sys

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from crews.models import Region
   from mm.models import Consumer
   from adm.models import Sheet, Type
   from datetime import datetime
   from analysis.models import RelatorioQuedaDeConsumo
   from mm.models import Consumer
   from analysis.models import Company

   Cemar = Company.objects.get(name='Cemar')
   
   wb = load_workbook("/home/tomash/painelcc/planilhas/20170503_baixar_em_lote.xlsx")
   ws = wb['Plan1']

   contador = 0

   for i in ws:
      if contador != 0:
         installation = str(i[0].value)
         dia = datetime.strptime(str(i[2].value)[0:10],"%Y-%m-%d")                        

	 reports = RelatorioQuedaDeConsumo.objects.all().filter(consumer = Consumer.objects.get(installation=installation,company=Cemar)).filter(referencia__day=dia.day).filter(referencia__month=dia.month).filter(referencia__year=dia.year)
         atualizar = reports.first()
         
         print str(installation) + "\t" + str(dia) + "\t" + str(len(reports))           
         
         if int(contador) % 2 == 0:
            user = "clai"
         else:
            user = "allas"

         atualizar.justificado = True
         atualizar.user = user
         atualizar.justificativa = "Baixado em Lote"
         atualizar.data_expira = "2017-03-30"
         atualizar.data_hora = "2017-03-30 00:00"
         atualizar.save()
         
         print "oi"
         
   
      contador += 1