from openpyxl import load_workbook
from django.core.wsgi import get_wsgi_application
from datetime import datetime
from sets import Set

import os
import sys

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from mm.models import MeterHistory, Meter, Consumer

   data_base = datetime.strptime("01/01/2017","%d/%m/%Y")

   historys = MeterHistory.objects.all().filter(until__year=2099).order_by('consumer')

   data_em_aberto = dict()

   for h in historys:
      try:
         data_em_aberto[h.consumer].append(h)
      except KeyError:
         data_em_aberto[h.consumer] = []
         data_em_aberto[h.consumer].append(h)
   
   consumers = Set([])

   for i in data_em_aberto:
      if len(data_em_aberto[i]) == 3:
         print i.installation
         if data_em_aberto[i][0].since < data_em_aberto[i][1].since:
            #print "primeiro"
            registro = MeterHistory.objects.all().get(id = data_em_aberto[i][0].id)
            registro.until = data_em_aberto[i][1].since

         #   registro.save()
         else:
            #print "segundo"
            registro = MeterHistory.objects.all().get(id = data_em_aberto[i][1].id)
            registro.until = data_em_aberto[i][0].since
          #  registro.save()
         
         
   print len(consumers)
   print len(data_em_aberto)