from django.core.wsgi import get_wsgi_application
from datetime import datetime, timedelta, tzinfo
import os, sys
import math

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from analysis.models import Billing, Inspection, RelatorioAlteracoesMedidor, RelatorioCorrenteZerada, RelatorioTensaoZerada, RelatorioMMVersusConsumo, RelatorioQuedaDeConsumo
   from mm.models import Consumer, Mm, Quantity, MeterHistory, History, Change, Company
   from django.db.models import Q

   meses = []

   inicio = datetime.strptime("01/06/2016","%d/%m/%Y")
   agora  = datetime.now()

   while inicio.month != agora.month or inicio.year != agora.year:
      meses.append(inicio)

      if inicio.month == 12:
         inicio = inicio.replace(month = 1)
         inicio = inicio.replace(year = inicio.year + 1)
      else:
         inicio = inicio.replace(month = inicio.month + 1)

   meses.append(inicio.replace(month=agora.month).replace(year=agora.year))

   companies = Company.objects.all().filter(name='Cemar')


   deletar = []

   for company in companies:
      print company.name

      consumers = []      

      relatorio_queda_consumo = RelatorioQuedaDeConsumo.objects.all().filter(justificado = False).filter(consumer__company=company)
      for rqc in relatorio_queda_consumo:
            billings = Billing.objects.all().filter(consumer=rqc.consumer).filter(reference__month = rqc.referencia.month).filter(reference__year = rqc.referencia.year)

            faturado = 0

            for bill in billings:
               faturado = faturado+bill.billed

            media_anterior = 0

            mes = rqc.referencia.month
            ano = rqc.referencia.year

            mes_anterior = mes - 3
            
            if mes_anterior <= 0:
               mes_anterior = mes_anterior + 12
               ano_anterior = ano - 1
            else:
               ano_anterior = ano

            if mes < 10:
               mes = "0"+str(mes)
            else:
               mes = str(mes)

            if mes_anterior < 10:
               mes_anterior = "0"+str(mes_anterior)
            else:
               mes_anterior = str(mes_anterior)

            inicio = datetime.strptime("01/"+mes_anterior+"/"+str(ano_anterior),"%d/%m/%Y")
            fim  = datetime.strptime("01/"+mes+"/"+str(ano),"%d/%m/%Y")

	    billings = Billing.objects.all().filter(consumer=rqc.consumer).filter(reference__gte = inicio).filter(reference__lt = fim)

            for bill in billings:
               media_anterior = media_anterior+bill.billed

            media_anterior = media_anterior/3

            if faturado > 0.8*media_anterior:
               deletar.append(rqc.id)


   for i in deletar:
      a = RelatorioQuedaDeConsumo.objects.get(id=i)
      a.delete()
