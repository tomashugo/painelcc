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

   alvos_em_aberto = Type.objects.get(type="Alvos Em Aberto")
   planilhas = Sheet.objects.all().filter(type=alvos_em_aberto).filter(processed=False)


   # deletar alvos que ainda nao foram despachados

   if len(planilhas) > 0:
      alvos = AlvosAbertos.objects.all()

      for i in alvos:
         despachado = AlvosDespachados.objects.all().filter(alvo_aberto=i)

         if len(despachado) == 0:
            i.delete()

   for p in planilhas:
      company = p.company

      wb = load_workbook(filename=p.path)
      ws = wb['Exportar Planilha']

      x = 0

      for i in ws:
         if x > 0:
            nota_servico = str(i[0].value)

            if nota_servico != "None":
               print nota_servico

            try:
               data_geracao = i[1].value.split('/')
       	       data_geracao = datetime.datetime(int(data_geracao[2])+2000, int(data_geracao[1]), int(data_geracao[0]))
            except AttributeError:
               continue

            instalacao = str(int(i[2].value))
            print "instalacao " + str(instalacao)

	    try:
               consumer = Consumer.objects.all().get(installation = instalacao,company__name='Cemar')
            except Consumer.DoesNotExist:
               print "Cliente com instalacao " + str(instalacao) + " nao existente"

            try:
               observacao  = i[6].value
            except AttributeError:
               observacao = "Nada"

            alvos_abertos = AlvosAbertos.objects.all().filter(ns=nota_servico).filter(consumer=consumer)	

            if len(alvos_abertos) == 0:
               #print consumer
               inspection,created = AlvosAbertos.objects.get_or_create(consumer=consumer,ns=nota_servico,data_geracao=data_geracao,observacao=observacao)
               #print "salvo"

         x = x + 1

      p.processed = True
      p.save()
