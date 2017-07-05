from django.core.wsgi import get_wsgi_application
from datetime import datetime, timedelta, tzinfo
import os, sys
import math

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from analysis.models import Billing, Inspection, RelatorioAlteracoesMedidor, RelatorioCorrenteZerada, RelatorioTensaoZerada, RelatorioMMVersusConsumo
   from mm.models import Consumer, Mm, Quantity, MeterHistory, History, Change, Company
   from django.db.models import Q

   qia = Quantity.objects.get(quantity = 'Ia')
   qib = Quantity.objects.get(quantity = 'Ib')
   qic = Quantity.objects.get(quantity = 'Ic')

   class Output(object):
      pass

   class Periodo(object):
      pass

   outputs = []

   a = datetime.strptime("01/01/16","%d/%m/%y")

   now = datetime.now()
   meses = []

   while a.month != now.month or a.year != now.year:
      meses.append(a)
      if a.month != 12:
         a = a.replace(month=a.month+1)
      else:
         a = a.replace(month=1,year=a.year+1)

   companies = Company.objects.all()

   for company in companies:

      consumers = Consumer.objects.all().filter(company=company)

      for cons in consumers:
         history = History.objects.all().filter(consumer=cons).filter(channel_1_qty = qia).filter(channel_2_qty = qib).filter(channel_3_qty = qic).order_by('date_hour')

         outputs = []

         output = Output()
         output.consumer = cons
         output.instalacao = cons.installation
         output.nome = cons.name
         output.id = cons.id

         zerado = False

         output.periodos = []

         for h in history:
            hora = h.date_hour

            if h.channel_1_value == 0 or h.channel_2_value == 0 or h.channel_3_value == 0:
               if zerado == False:
                  zerado = True
                  a = Periodo()
                  a.hora_inicio = hora
                  a.ia = h.channel_1_value
                  a.ib = h.channel_2_value
                  a.ic = h.channel_3_value
                  output.periodos.append(a)
            else:
               if zerado == True:
                  zerado = False
                  output.periodos[-1].hora_fim = hora

                  dif = hora-output.periodos[-1].hora_inicio

                  if dif.seconds < 3600*6:
                     print "pop"
                     output.periodos.pop()
        

         if len(output.periodos):
            output.periodos.first().hora_fim = output.periodos.first().hora_inicio

         outputs.append(output)      

         for output in outputs:
            for periodo in output.periodos:
               relatorio_corrente_zerada = RelatorioCorrenteZerada.objects.all().filter(consumer = output.consumer).filter(inicio = periodo.hora_inicio).filter(ia = periodo.ia).filter(ib = periodo.ib).filter(ic = periodo.ic)
               #print "hora inicio: " + str(periodo.hora_inicio) + " " + str(periodo.hora_fim)
               if len(relatorio_corrente_zerada) == 0:
                  relatorio_corrente_zerada = RelatorioCorrenteZerada()
                  relatorio_corrente_zerada.consumer = output.consumer
                  relatorio_corrente_zerada.inicio = periodo.hora_inicio
                  relatorio_corrente_zerada.ia = periodo.ia
                  relatorio_corrente_zerada.ib = periodo.ib
                  relatorio_corrente_zerada.ic = periodo.ic
                  relatorio_corrente_zerada.expira = True
                  relatorio_corrente_zerada.justificado = False
                  relatorio_corrente_zerada.company = company

                  try:
                     relatorio_corrente_zerada.fim = periodo.hora_fim
                  except AttributeError:
                     data_ate = periodo.hora_inicio + timedelta(days=30)
     	             relatorio_corrente_zerada.fim = data_ate

                  relatorio_corrente_zerada.save()

