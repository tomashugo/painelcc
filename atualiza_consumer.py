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
            public_place = i[4].value.encode('utf-8')
         except AttributeError:
            public_place = ""

         try:
            reference = i[5].value.encode('utf-8')
         except AttributeError:
            reference = ""

         try:
            complement = i[6].value.encode('utf-8')
         except AttributeError:
            complement = ""

         try:
            region = i[7].value.encode('utf-8')
         except AttributeError:
            region = "UNDEF"

         try:
            revenue = i[8].value.encode('utf-8')
         except AttributeError:
            revenue = "#"

         if installation != 'UC':
            print region
            region = Region.objects.get(name=region)
	    already_installed = Consumer.objects.filter(company=company,installation=installation)

	    if len(already_installed) == 1:
               consumer = already_installed.first()
                        
               consumer.reference = reference
               consumer.public_place = public_place
               consumer.complement = complement
            
               consumer.save()
