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

   inspecao = Type.objects.get(type="Inspecao")
   planilhas = Sheet.objects.all().filter(type=inspecao).filter(processed=False)

   for p in planilhas:
      company = p.company


      wb = load_workbook(filename=p.path)
      ws = wb['Exportar Planilha']

      x = 0

      for i in ws:
         if x > 0:

            installation = str(int(i[0].value))
            ns = i[1].value

            try:
               code = str(int(i[2].value))
            except ValueError:
               code = "300"
            except TypeError:
               code = "300"

            try:
               date_time_executed = i[3].value.split('/')
       	       date_time_executed = datetime.datetime(int(date_time_executed[2])+2000, int(date_time_executed[1]), int(date_time_executed[0]))
            except AttributeError:
               continue

            try:
               date_time_competence = i[4].value.split('/')
      	       date_time_competence = datetime.datetime(int(date_time_competence[2])+2000, int(date_time_competence[1]),int(date_time_competence[0]))
            except AttributeError:
               date_time_competence = datetime.datetime(date_time_executed.year,date_time_executed.month,date_time_executed.day)


            try:
               observation  = i[5].value
            except AttributeError:
               observation = "Nada"

   	    if observation is None:
               observation = "Nada"

            try:
               date_time_load = i[6].value.split('/')
   	       date_time_load = datetime.datetime(int(date_time_load[2])+2000, int(date_time_load[1]), int(date_time_load[0]))
            except AttributeError:
               date_time_load = i[6].value

            try:
               consumer = Consumer.objects.get(installation=installation,company=company)
               inspections = Inspection.objects.all().filter(ns=ns).filter(consumer=consumer)
               if len(inspections) == 0:
                  print consumer
                  inspection,created = Inspection.objects.get_or_create(consumer=consumer,ns=ns,observation=observation,date_time_executed=date_time_executed,date_time_competence=date_time_competence,code=code,date_time_load=date_time_load)
                  #created.save()
            except Consumer.DoesNotExist:
               print "Cliente com instalacao " + str(installation) + " nao existente"

         x = x + 1

      p.processed = True
      p.save()
