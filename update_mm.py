from django.core.wsgi import get_wsgi_application

import os
import sys

from datetime import tzinfo, timedelta,datetime

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from crews.models import Region
   from mm.models import Consumer, Meter, MeterHistory, Mm, Quantity, EnergyFault, History, Change, Holiday

#   correntes_erradas = Mm.objects.all().filter(channel_1_qty = Quantity.objects.get(quantity = 'Ia')).filter(constant1='000001/000080')
   tensoes_erradas = Mm.objects.all().filter(channel_1_qty = Quantity.objects.get(quantity = 'Va')).filter(constant1='000001/002000')

   new_channel_1_qty = Quantity.objects.get(quantity='Va')
   new_channel_2_qty = Quantity.objects.get(quantity='Vb')
   new_channel_3_qty = Quantity.objects.get(quantity='Vc')

   for i in tensoes_erradas:
      history = History.objects.all().filter(mm=i)

      i.channel_1_qty = new_channel_1_qty
      i.channel_2_qty = new_channel_2_qty
      i.channel_3_qty = new_channel_3_qty
      i.save()

      for j in history:
          j.channel_1_qty = new_channel_1_qty
          j.channel_2_qty = new_channel_2_qty
          j.channel_3_qty = new_channel_3_qty
          j.save()


#   correntes_erradas = Mm.objects.all().filter(channel_1_qty = Quantity.objects.get(quantity = 'Ia')).filter(constant1='000001/000080')

#   new_channel_1_qty = Quantity.objects.get(quantity='Va')
#   new_channel_2_qty = Quantity.objects.get(quantity='Vb')
#   new_channel_3_qty = Quantity.objects.get(quantity='Vc')

#   for i in correntes_erradas:
#      history = History.objects.all().filter(mm=i)

#      i.channel_1_qty = new_channel_1_qty
#      i.channel_2_qty = new_channel_2_qty
#      i.channel_3_qty = new_channel_3_qty
#      i.save()

#      for j in history:
#          j.channel_1_qty = new_channel_1_qty
#          j.channel_2_qty = new_channel_2_qty
#          j.channel_3_qty = new_channel_3_qty
#          j.save()
