from django.core.wsgi import get_wsgi_application

import os
import sys
import re

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from mm.models import Unprocessed

   objetos = Unprocessed.objects.all()

   casos_encontrados = 0

   for obj in objetos:
      regex = re.search('Medidor 3314([0-9]{6}) Nao Encontrado',obj.msg)
      if regex:
         casos_encontrados = casos_encontrados + 1
         print obj.msg
         print obj.archive

   print  str(casos_encontrados) + " casos encontrados"
