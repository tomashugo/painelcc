from django.core.wsgi import get_wsgi_application
from datetime import datetime, timedelta, tzinfo
import os, sys
import math

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from analysis.models import Billing, Inspection, RelatorioAlteracoesMedidor, RelatorioCorrenteZerada, RelatorioTensaoZerada, RelatorioMMVersusConsumo
   from mm.models import Consumer, Mm, Quantity, MeterHistory, History, Change, Company
   from django.db.models import Q

   relatorio_tensao_zerada = RelatorioTensaoZerada.objects.all().filter(justificado=False).order_by('consumer','inicio','va','vb','vc')

   anterior = relatorio_tensao_zerada.first()

   for i in relatorio_tensao_zerada:
      if i != relatorio_tensao_zerada.first():
         print str(i.consumer) + " " + str(i.inicio) + " " + str(i.va) + " " + str(i.vb) + " " + str(i.vc)
         if (anterior.consumer == i.consumer) and (anterior.inicio == i.inicio) and (anterior.va == i.va) and (anterior.vb == i.vb) and (anterior.vc == i.vc):
            anterior.delete()
            #anterior.save()
            print "##########Anterior deletado##########"


      anterior = i
