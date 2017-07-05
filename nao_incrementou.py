from openpyxl import load_workbook
from django.core.wsgi import get_wsgi_application
from datetime import datetime

import os
import sys

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from django.db.models import Q
   from crews.models import Region
   from mm.models import Consumer, Company
   from adm.models import Sheet, Type
   from analysis.models import Inspection, Billing, RelatorioFraudeNaoIncrementada

   ano_2015 = datetime.strptime("01/01/2015","%d/%m/%Y")

   empresas = Company.objects.all()

   for empresa in empresas:

      normalizacoes = Inspection.objects.all().filter(code__startswith = '1').filter(consumer__company=empresa).filter(date_time_executed__gte = ano_2015)

      for i in normalizacoes:
         cmp_inspecao = i.date_time_executed

         mes_posterior = cmp_inspecao.month + 1
         mes_anterior = cmp_inspecao.month - 1

         ano_anterior = cmp_inspecao.year
         ano_posterior = cmp_inspecao.year

         if mes_posterior == 13:
            mes_posterior = 1
            ano_posterior = ano_posterior + 1

         if mes_anterior == 0:
            mes_anterior = 12
            ano_anterior = ano_anterior - 1

         faturamento_antes = Billing.objects.all().filter(reference__month = mes_anterior).filter(reference__year = ano_anterior).filter(consumer=i.consumer)
         faturamento_apos = Billing.objects.all().filter(reference__month = mes_posterior).filter(reference__year = ano_posterior).filter(consumer=i.consumer)

         faturamento_anterior = 0

         if len(faturamento_antes) == 0 or len(faturamento_apos) == 0:
            continue

         for f in faturamento_antes:
            faturamento_anterior = faturamento_anterior + f.billed

         faturamento_posterior = 0

         for f in faturamento_apos:
            faturamento_posterior = faturamento_posterior + f.billed

         if faturamento_posterior < faturamento_anterior*1.2:
            print str(i.consumer.installation) + "\t" + str(i.code) + "\t" + str(i.date_time_executed) + "\t" + str(faturamento_anterior) + "\t" + str(faturamento_posterior)

            existe = RelatorioFraudeNaoIncrementada.objects.all().filter(company=empresa,consumer=i.consumer,mes_fraude=i.date_time_executed,code_fraude=i.code,faturamento_anterior=faturamento_anterior,faturamento_posterior=faturamento_posterior)

            if len(existe) == 0:
               relatorio = RelatorioFraudeNaoIncrementada()

               relatorio.justificado = False
               relatorio.company = empresa
               relatorio.consumer = i.consumer
               relatorio.mes_fraude = i.date_time_executed
               relatorio.code_fraude = i.code
               relatorio.faturamento_anterior = faturamento_anterior
               relatorio.faturamento_posterior = faturamento_posterior

               relatorio.save()
 
