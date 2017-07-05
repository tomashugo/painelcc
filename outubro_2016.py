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

   from analysis.models import Directory, Billing, Register, RelatorioQuedaDeConsumo
   from django.db import models
   from crews.models import Region
   from mm.models import Consumer, Meter, MeterHistory, Mm, Quantity, EnergyFault, History, Change, Holiday, Unprocessed, Company

   consumers = Consumer.objects.all().filter(company=Company.objects.get(name='Cemar'))

   ref_09_2016 = datetime.strptime("01/09/2016","%d/%m/%Y")
   ref_10_2016 = datetime.strptime("01/10/2016","%d/%m/%Y")

   quantidade = 0

   for con in consumers:
      setembro = Billing.objects.all().filter(consumer=con).filter(reference=ref_09_2016)
      outubro = Billing.objects.all().filter(consumer=con).filter(reference=ref_10_2016)

      if (len(setembro) != len(outubro)) and len(outubro) ==4:
         print str(con.installation) + "\t" + str(len(setembro)) + "\t" + str(len(outubro))
         energia_ponta = outubro.filter(code_type=Register.objects.get(code='EAP'))
         energia_f_ponta = outubro.filter(code_type=Register.objects.get(code='EAFP'))

         queda_consumo_outubro = RelatorioQuedaDeConsumo.objects.all().filter(referencia=ref_10_2016)

         if len(queda_consumo_outubro) > 0:
            #queda_consumo_outubro.last().delete()
            print "Queda consumo deletado"

         if len(energia_ponta) == 2:
            #energia_ponta.last().delete()
            print "Energia ponta deletado"

         if len(energia_f_ponta) == 2:
            #energia_f_ponta.last().delete()
            print "Energia fora ponta deletado"

   print quantidade
