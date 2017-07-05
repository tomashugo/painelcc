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
   from mm.models import Consumer
   from analysis.models import Inspection

   wb = load_workbook(filename='upload/inspecoes_2016.xlsx')
   ws = wb['Exportar Planilha']

   x = 0

   for i in ws:
      if x > 0:

         installation = str(int(i[0].value))
         nota_de_servico = i[1].value

         try:
            code = str(int(i[2].value))
         except ValueError:
            code = "300"

         date_time_executed = i[3].value.split('/')
	 date_time_executed = datetime.datetime(int(date_time_executed[2])+2000, int(date_time_executed[1]), int(date_time_executed[0]))

         date_time_competence = i[4].value.split('/')
	 date_time_competence = datetime.datetime(int(date_time_competence[2])+2000, int(date_time_competence[1]),int(date_time_competence[0]))

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
            inspection = Inspection.objects.all().filter(ns=nota_de_servico)
            inspection = inspection.first()
            inspection.observation = observation
            inspection.save()
            print "Laudo nspecao " + nota_de_servico + " atualizado"
         except AttributeError:
            print "Inspecao " + nota_de_servico + " nao estava cadastrada"

      x = x + 1
