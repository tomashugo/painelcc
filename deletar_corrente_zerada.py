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

   relatorio_corrente_zerada = RelatorioCorrenteZerada.objects.all().filter(justificado=False).order_by('consumer','inicio','ia','ib','ic')

   anterior = relatorio_corrente_zerada.first()

   for i in relatorio_corrente_zerada:
      if i != relatorio_corrente_zerada.first():
         print str(i.consumer) + " " + str(i.inicio) + " " + str(i.ia) + " " + str(i.ib) + " " + str(i.ic)
         if (anterior.consumer == i.consumer) and (anterior.inicio == i.inicio) and (anterior.ia == i.ia) and (anterior.ib == i.ib) and (anterior.ic == i.ic):
            anterior.delete()
            #anterior.save()
            print "##########Anterior deletado##########"


      anterior = i
