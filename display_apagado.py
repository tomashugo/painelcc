from django.core.wsgi import get_wsgi_application
from datetime import datetime, timedelta, tzinfo
import os, sys
import math

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from analysis.models import Billing, Inspection, RelatorioAlteracoesMedidor, RelatorioCorrenteZerada, RelatorioTensaoZerada, RelatorioMMVersusConsumo
   from mm.models import Consumer, Mm, Quantity, MeterHistory, History, Change
   from django.db.models import Q


   consumer = Consumer.objects.all().get(installation = 5276500)

   trocas_medidor = Inspection.objects.all().filter(observation__icontains = 'APAGADO').filter(code = '201').filter(consumer=consumer)

   print "Trocas Medidor"

   for troca in trocas_medidor:
      meter_history = MeterHistory.objects.all().filter(consumer=troca.consumer)

      print troca.consumer.installation + "\t" + troca.consumer.name
      

      for history in meter_history:
         print "Executed: \t" + str(troca.date_time_executed) + "\t" + str(history.since)