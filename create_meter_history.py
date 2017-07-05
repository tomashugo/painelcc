from openpyxl import load_workbook
from django.core.wsgi import get_wsgi_application

import os
import sys
from multiplicador import multiplicador

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from crews.models import Region
   from mm.models import Consumer, Meter, MeterHistory
   from adm.models import Type,Sheet
   import datetime

   medidores = Type.objects.get(type="Medidores")
   planilhas = Sheet.objects.all().filter(type=medidores).filter(processed=False)

   for p in planilhas:
      company = p.company
      wb = load_workbook(filename=p.path)
      ws = wb['Exportar Planilha']
      print p.path

      linha_planilha = 0

      for i in ws:
         if linha_planilha != 0:
            installation = str(i[0].value)
            serial = str(i[1].value)
            dateto = str(i[2].value)
            datefrom = str(i[3].value)

            dateto = dateto.split('/')
            datefrom = datefrom.split('/')

            print installation + "\t" + serial

            dateto[2] = "20"+dateto[2]
            datefrom[2] = "20"+datefrom[2]

            s = "/"

   	    dateto = datetime.datetime.strptime(s.join(dateto), "%d/%m/%Y")
            datefrom = datetime.datetime.strptime(s.join(datefrom), "%d/%m/%Y")

            try:
               if len(serial) == 10:
                  serial = serial + str(multiplicador(serial))
            except ValueError:
               continue

            print "serial: " + serial
            consumer = Consumer.objects.filter(company=company,installation=installation)
            meter, created = Meter.objects.get_or_create(company=company,serial=serial)


            if len(consumer) > 0:
               consumer = consumer.first()

               until_dumb = datetime.datetime.strptime("31/12/2099","%d/%m/%Y")
               test = MeterHistory.objects.all().filter(meter=meter).filter(consumer=consumer).filter(since=datefrom).filter(until=until_dumb)

               if len(test) == 0:
                  meter_history, created = MeterHistory.objects.get_or_create(meter=meter,consumer=consumer,until=dateto,since=datefrom)
                  if created:
                     meter_history.save()
               else:
                  if dateto != until_dumb:
                     print "entrou aqui"
                     meter_history = test.first()
                     meter_history.until = dateto
                     meter_history.save()

         linha_planilha += 1
         print "linha final"

      p.processed = True
      p.save()
