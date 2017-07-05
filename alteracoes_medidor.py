from django.core.wsgi import get_wsgi_application
from datetime import datetime, timedelta, tzinfo
from django.db.models import Q
import os, sys
import math

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from analysis.models import Billing, Inspection, RelatorioAlteracoesMedidor, RelatorioCorrenteZerada, RelatorioTensaoZerada, RelatorioMMVersusConsumo
   from mm.models import Consumer, Mm, Quantity, MeterHistory, History, Change

   a = datetime.strptime("01/01/16","%d/%m/%y")

   now = datetime.now()
   meses = []

   while a.month != now.month or a.year != now.year:
      meses.append(a)
      if a.month != 12:
         a = a.replace(month=a.month+1)
      else:
         a = a.replace(month=1,year=a.year+1)

   for mes in meses:
      changes = Change.objects.all().filter(date_time__month = mes.month).filter(date_time__year = mes.year).filter(~Q(code='20')).order_by('date_time')

      class Output(object):
         pass
   
      outputs = []
 
      for change in changes:
         meter_history = MeterHistory.objects.all().filter(since__lte = change.date_time).filter(until__gte = change.date_time).filter(meter=change.meter)
      
         if len(meter_history) > 0:
            consumer = meter_history.first().consumer

            output = Output()
  
            output.code = change.code
            output.observacao = change.observation
            output.consumer_id = consumer.id
            output.data = change.date_time
            output.instalacao = consumer.installation
            output.nome = consumer.name
            output.leitor = change.leitor

            inspection = Inspection.objects.all().filter(date_time_executed__day = change.date_time.day).filter(date_time_executed__month = change.date_time.month).filter(date_time_executed__year = change.date_time.year).filter(consumer = consumer)

            if len(inspection) > 0:
               output.inspecao = "SIM"
            else:
               output.inspecao = "NAO"

            billing = Billing.objects.all().filter(end_cycle__day = change.date_time.day).filter(end_cycle__month = change.date_time.month).filter(end_cycle__year = change.date_time.year).filter(consumer=consumer)

            if len(billing) > 0:
               output.leitura = "SIM"
            else:
               output.leitura = "NAO"

            if output.inspecao == 'NAO' and output.leitura == 'NAO': 
               output.acao = 'CHECAR'
	       relatorio = RelatorioAlteracoesMedidor.objects.all().filter(consumer = consumer).filter(data_alteracao = change.date_time).filter(leitor = change.leitor).filter(code = change.code).filter(observacao = change.observation)

               if len(relatorio) == 0:
                  relatorio = RelatorioAlteracoesMedidor()
                  relatorio.consumer = consumer
                  relatorio.data_alteracao = change.date_time
                  relatorio.leitor = change.leitor
                  relatorio.code = change.code
                  relatorio.observacao = change.observation
                  relatorio.justificado = False
                  relatorio.expira = True
                  relatorio.save()

            else: 
               output.acao = '-'
         
            outputs.append(output)

