# -*- coding: utf-8 -*-
from openpyxl import load_workbook
from django.core.wsgi import get_wsgi_application

import os
import sys
import datetime

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from crews.models import Region
   from mm.models import Consumer, Company
   from analysis.models import Inspection
   from adm.models import Type, Sheet
   from producao.models import AlvosAbertos, AlvosDespachados

   alvos_cancelados = Type.objects.get(type="Alvos Cancelados")
   planilhas = Sheet.objects.all().filter(type=alvos_cancelados).filter(processed=False)

   for p in planilhas:
      company = p.company

      wb = load_workbook(filename=p.path)
      ws = wb['Exportar Planilha']

      x = 0
      
      contador = 0

      # laco for nas linhas da planilha
      for i in ws:
         if x > 0:
            nota_servico = str(i[0].value)

            alvo_aberto = AlvosAbertos.objects.all().filter(ns=nota_servico)
            
            if len(alvo_aberto) == 1:
                alvo_aberto = alvo_aberto.first()
                
                alvos_despachados = AlvosDespachados.objects.all().filter(alvo_aberto=alvo_aberto)
                
                for ad in alvos_despachados:
                    ad.delete()
                    contador = contador + 1
                
         x = x + 1       
            
            
      p.processed = True
      p.save()
      
      
   print "Alvos deletados " + str(contador)
      
