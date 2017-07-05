from django.core.wsgi import get_wsgi_application

import os
import sys
from codes import code_alteracao


from datetime import tzinfo, timedelta,datetime

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from crews.models import Region
   from mm.models import Consumer, Meter, MeterHistory, Mm, Quantity, EnergyFault, History, Change, Holiday

   UTCm3 = timedelta(hours=-3)

   class UTC(tzinfo):
      def utcoffset(self,dt):
         return UTCm3
      def dst(self,dt):
         return UTCm3
      def tzname(self,dt):
         return "UTC-3"

   utc = UTC()

#   nome_diretorio = "upload/mm"
#   arquivos = os.listdir(nome_diretorio)

#   contador = 1

#   for arq in arquivos:
#      caminho_arq = nome_diretorio + "/" + arq

#      print arq + " " + str(contador)
#      contador = contador+1

#      mms = Mm.objects.filter(archive=arq)

#      if len(mms) == 0:
#         continue

#      mm_string = ""
#      for linhas in open(caminho_arq):
#         mm_string = mm_string + linhas.split('\r\n')[0]

#      medidor = "33" + mm_string[0:8]
#      medidor_ = Meter.objects.filter(serial__startswith=medidor)

#      if len(medidor_) == 0:
#         continue

#      leitor = mm_string[8:14]

      # inserindo alteracoes no medidor
#      i = 0
#      initial = 1906

#      while i < 16:
#         print "."
#         try: 
#            codigo_alteracao = str(mm_string[initial:initial+2])
#            leitor_alteracao = str(mm_string[initial+2:initial+8])
#            hora_alteracao = int(mm_string[initial+8:initial+10])
#            minuto_alteracao = int(mm_string[initial+10:initial+12])
#            segundo_alteracao = int(mm_string[initial+12:initial+14])
#            dia_alteracao = int(mm_string[initial+14:initial+16])
#            mes_alteracao = int(mm_string[initial+16:initial+18])
#            ano_alteracao = 2000 + int(mm_string[initial+18:initial+20])

#            alteracao = datetime(ano_alteracao,mes_alteracao,dia_alteracao,hora_alteracao,minuto_alteracao,segundo_alteracao,0,utc)
#            obj, created = Change.objects.get_or_create(code=codigo_alteracao,observation=code_alteracao[int(codigo_alteracao)],meter=medidor_.first(),leitor=leitor_alteracao,date_time=alteracao)
#            print "depois"
#            if created:
#               obj.save()
#               print "inserido!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#         except ValueError:
#            i = 17
#            continue        
#         except KeyError:
#            i = 17
#            continue

#         initial = initial + 20
#         i = i + 1

 
