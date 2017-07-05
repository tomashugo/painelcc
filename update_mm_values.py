from django.core.wsgi import get_wsgi_application
from django.db.models import Q

import os
import sys

from datetime import tzinfo, timedelta,datetime

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from crews.models import Region
   from mm.models import Consumer, Meter, MeterHistory, Mm, Quantity, EnergyFault, History, Change, Holiday

   historys = History.objects.all().filter(Q(channel_1_pulse__gt = 2048) | Q(channel_2_pulse__gt = 2048) | Q(channel_3_pulse__gt = 2048))

   print str(len(historys)) + " ocorrencias "

   for h in historys:
      #print str(h.mm.archive) + "\t" + str(h.channel_1_qty.quantity) + "\t" + str(h.channel_2_qty.quantity) + "\t" + str(h.channel_3_qty.quantity)
      #print "Antes       " + "\t" + str(h.channel_1_value) + "\t" + str(h.channel_2_value) + "\t" + str(h.channel_3_value)

      numerador1 = float(h.mm.constant1.split('/')[0])
      denominador1 = float(h.mm.constant1.split('/')[1])
      cte1 = numerador1/denominador1

      numerador2 = float(h.mm.constant2.split('/')[0])
      denominador2 = float(h.mm.constant2.split('/')[1])
      cte2 = numerador2/denominador2

      numerador3 = float(h.mm.constant3.split('/')[0])
      denominador3 = float(h.mm.constant3.split('/')[1])
      cte3 = numerador3/denominador3

      valor1 = (2048 - h.channel_1_pulse)*cte1
      valor2 = (2048 - h.channel_2_pulse)*cte2
      valor3 = (2048 - h.channel_3_pulse)*cte3

      h.channel_1_value = valor1
      h.channel_2_value = valor2
      h.channel_3_value = valor3
      h.save()

      #print "Depois" + "\t" + str(valor1) + "\t" + str(valor2) + "\t" + str(valor3)

      #print ""
      #print ""