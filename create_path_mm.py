from django.core.wsgi import get_wsgi_application
from django.db.models import Q
from codes import code_alteracao
from django.core.exceptions import MultipleObjectsReturned

import os
import sys

from datetime import tzinfo, timedelta,datetime

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from crews.models import Region
   from mm.models import Consumer, Meter, MeterHistory, Mm, Quantity, EnergyFault, History, Change, Holiday

   nome_diretorio = "/home/tomash/painelcc/upload/mm"
   arquivos = os.listdir(nome_diretorio)

   quantidade_arquivos = 1

   for arq in arquivos:
      results = Mm.objects.all().filter(archive = arq)
      
      if len(results) > 0:
         for res in results:
            res.path = nome_diretorio + "/" + arq
            res.save()
