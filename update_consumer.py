from openpyxl import load_workbook
from django.core.wsgi import get_wsgi_application

import os
import sys

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from crews.models import Region
   from mm.models import Consumer
   from adm.models import Sheet, Type

   consumidores = Type.objects.get(type="Consumidores")
   planilhas = Sheet.objects.all().filter(type=consumidores).filter(processed=False)

   for p in planilhas:
      company = p.company
      wb = load_workbook(filename=p.path)
      ws = wb['Exportar Planilha']

      for i in ws:
         try:
            installation = str(i[0].value)
         except AttributeError:
            installation = ""

         try:
            name = i[1].value.encode('utf-8')
         except AttributeError:
            name = ""

         try:
            meter = str(i[2].value)
         except AttributeError:
            meter = ""

         try:
            city = i[3].value.encode('utf-8')
         except AttributeError:
            city = ""
  
         try:
            region = i[4].value.encode('utf-8')
         except AttributeError:
            region = "UNDEF"

         try:
            revenue = i[5].value.encode('utf-8')
         except AttributeError:
            revenue = "#"

         if installation != 'UC':
            print region
            region = Region.objects.get(name=region)
	    already_installed = Consumer.objects.filter(company=company,installation=installation)

	    if len(already_installed) == 0:
	       consumer = Consumer()

               consumer.company = company
               consumer.installation = installation
               consumer.name = name
               consumer.meter = meter
               consumer.city = city
               consumer.region = region
	       consumer.revenue = revenue[0]

               consumer.save()

	       #print installation + " " + name + " " + meter + " " + city + " " + str(region_id) + " " + revenue

      p.processed = True
      p.save()
