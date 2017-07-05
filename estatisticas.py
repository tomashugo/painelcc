from openpyxl import load_workbook
from django.core.wsgi import get_wsgi_application

import os
import sys

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from django.db.models import Q
   from crews.models import Region
   from mm.models import Consumer, Meter, MeterHistory, Company
   from analysis.models import Billing, Register
   from datetime import datetime
   from django.shortcuts import get_object_or_404
   from adm.models import Type, Sheet
   from analysis.models import RelatorioMMVersusConsumo, RelatorioAlteracoesMedidor, RelatorioCorrenteZerada, RelatorioTensaoZerada, RelatorioQuedaDeConsumo, Billing, Inspection, RelatorioFraudeNaoIncrementada
   from analysis.models import Inspection
   from producao.models import AlvosAbertos, AlvosDespachados, Producao

   company_session = Company.objects.get(name='Cemar')

   fraude_nao_incrementada = RelatorioFraudeNaoIncrementada.objects.all().filter(justificado=True).filter(company=company_session).filter(alvo_gerado=True).filter(~Q(justificativa__contains = '!BATCH'))
   relatorio_mm_versus_consumo = RelatorioMMVersusConsumo.objects.all().filter(justificado = True).filter(company=company_session).filter(alvo_gerado=True).filter(~Q(justificativa__contains = '!BATCH'))
   alteracoes_medidor = RelatorioAlteracoesMedidor.objects.all().filter(justificado = True).distinct('consumer').distinct('data_alteracao').filter(company=company_session).filter(alvo_gerado=True).filter(~Q(justificativa__contains = '!BATCH'))
   queda_consumo = RelatorioQuedaDeConsumo.objects.all().filter(justificado = True).filter(company=company_session).filter(alvo_gerado=True).filter(~Q(justificativa__contains = '!BATCH'))
   corrente_zerada = RelatorioCorrenteZerada.objects.all().filter(justificado = True).distinct('consumer').filter(company=company_session).filter(alvo_gerado=True).filter(~Q(justificativa__contains = '!BATCH'))
   tensao_zerada = RelatorioTensaoZerada.objects.all().filter(justificado = True).distinct('consumer').filter(company=company_session).filter(alvo_gerado=True).filter(~Q(justificativa__contains = '!BATCH'))
   
   alvos_gerados = len(fraude_nao_incrementada) + len(relatorio_mm_versus_consumo) + len(alteracoes_medidor) + len(queda_consumo) + len(corrente_zerada) + len(tensao_zerada)

   alarms = AlvosAbertos.objects.all()

   alvos_despachados = 0

   for alarm in alarms:
      despachados = AlvosDespachados.objects.all().filter(alvo_aberto = alarm)
      
      if len(despachados) > 0:
         alvos_despachados += 1


   print alvos_despachados
   print len(alarms) - alvos_despachados