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

   inicio = datetime.strptime("01/01/2017","%d/%m/%Y")
   agora  = datetime.now()
   #agora = datetime.strptime("01/07/2016","%d/%m/%Y")

   while inicio.month != agora.month or inicio.year != agora.year:
      meses.append(inicio)

      if inicio.month == 12:
         inicio = inicio.replace(month = 1)
         inicio = inicio.replace(year = inicio.year + 1)
      else:
         inicio = inicio.replace(month = inicio.month + 1)

   meses.append(inicio.replace(month=agora.month).replace(year=agora.year))

   companies = Company.objects.all()

   for company in companies:
      print company.name

      consumers = Consumer.objects.all().filter(company = company)

      for cons in consumers:
         mes_fat = []
         fat = []

         for mes in meses:
            billings = Billing.objects.all().filter(consumer=cons).filter(reference = mes)

            faturado = 0

            for bill in billings:
               faturado = faturado+bill.billed

            if len(billings) > 0:
               mes_fat.append(mes)
               fat.append(faturado)

            qnt = len(fat)

            if qnt > 4:
               consumo_ultimo_mes = fat[qnt-1]
               media_tres = 0

               indice = qnt-2

               while indice > qnt-5 and indice > 0:
                  media_tres = media_tres + fat[indice]
                  indice = indice-1

               media_tres = media_tres/3


               if consumo_ultimo_mes < 0.8*media_tres:
                  a = RelatorioQuedaDeConsumo.objects.all().filter(consumer=cons).filter(referencia=mes_fat[len(mes_fat)-1])
                  b = RelatorioQuedaDeConsumo.objects.all().filter(consumer=cons).filter(referencia__gte=mes_fat[len(mes_fat)-1]).filter(justificado=True)

                  if len(a) == 0 and len(b) == 0:
                     relatorio = RelatorioQuedaDeConsumo()

                     relatorio.consumer = cons
                     relatorio.referencia=mes_fat[len(mes_fat)-1]
                     relatorio.media_consumo = media_tres
      	             relatorio.consumo_referencia = consumo_ultimo_mes
                     relatorio.justificado = False
                     relatorio.company = company
                     relatorio.save()




