from django.core.wsgi import get_wsgi_application
from datetime import datetime, timedelta, tzinfo
import os, sys
import math

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from analysis.models import Billing, Inspection, RelatorioAlteracoesMedidor, RelatorioCorrenteZerada, RelatorioTensaoZerada, RelatorioMMVersusConsumo
   from mm.models import Consumer, Mm, Quantity, MeterHistory, History, Change, Company

   inicio_script = datetime.now()
   

   clientes = []

   class Cliente(object):
      pass

   class Rec(object):
      pass

   a = datetime.strptime("01/01/16","%d/%m/%y")

   now = datetime.now()
   meses = []

   UTCm3 = timedelta(hours=-3)

   class UTC(tzinfo):
      def utcoffset(self,dt):
         return UTCm3
      def dst(self,dt):
         return UTCm3
      def tzname(self,dt):
         return "UTC-3"

   utc = UTC()

   while a.month != now.month or a.year != now.year:
      meses.append(a)
      if a.month != 12:
         a = a.replace(month=a.month+1)
      else:
         a = a.replace(month=1,year=a.year+1)

   companies = Company.objects.all()

   for company in companies:
      consumers = Consumer.objects.all().filter(company=company)
   
   
      for cons in consumers:
         for mes in meses:
             cliente = Cliente()
             cliente.consumer = cons

             meter = MeterHistory.objects.all().filter(consumer=cons).filter(since__lte=mes).filter(until__gte=mes)

             if len(meter) > 0:
                cliente.medidor = meter.first().meter
             else:
                break

             bills = Billing.objects.all().filter(reference=mes).filter(consumer=cons)

             if len(bills) == 0:
                continue

             consumo = 0

             for b in bills:
                consumo = consumo + b.billed

             cliente.consumo_faturado = consumo

             ultimo_faturamento = bills.first().end_cycle
             penultimo_faturamento = bills.first().init_cycle

             recs = Mm.objects.all().filter(meter_object=meter.first().meter).filter(channel_1_qty=Quantity.objects.get(quantity='kW')).filter(last_bill__date=ultimo_faturamento).filter(penultimate_bill__date=penultimo_faturamento)

             add = True

             # clente do grupo B
             if len(recs) == 0:
                #print "cliente do grupo B"
                delta = ultimo_faturamento - penultimo_faturamento
                minutos = delta.days*24*60 + delta.seconds/60
                intervalos_5 = minutos/5

                if intervalos_5 == 0:
                   continue

                #print "intervalos_5 " + str(intervalos_5)

                historys = History.objects.all().filter(consumer=cons).filter(channel_1_qty=Quantity.objects.get(quantity='kW')).filter(date_hour__lte=ultimo_faturamento-timedelta(seconds=3600*3)).filter(date_hour__gte=penultimo_faturamento-timedelta(seconds=3*3600)).order_by('date_hour')

                consumo_mm = 0
                quantidade_intervalos = 0

                data_hora_anterior = datetime(1900,1,1,1,1,1,0,utc)

                for h in historys:
                   if data_hora_anterior != h.date_hour:
                      if (h.date_hour-data_hora_anterior).seconds >= 300:
                         consumo_mm = consumo_mm + h.channel_1_value*1/12
                         data_hora_anterior = h.date_hour
                         quantidade_intervalos = quantidade_intervalos + 1

                         #print str(h.date_hour-timedelta(seconds=3600*3)) + "\t" + str(h.mm.archive) + "\t" + str(h.channel_1_pulse) + "\t" + str(h.channel_1_value) + "\t" + str(h.channel_1_value*1/12) + "\t" + str(consumo_mm)

                #print "quantidade_intervalos " + str(quantidade_intervalos)

                dif_intervalos = (quantidade_intervalos - intervalos_5)/intervalos_5*100

                cliente.recs = []

                #print dif_intervalos
                print consumo
                print consumo_mm

                if math.fabs(dif_intervalos) < 10:
                   r = Rec()
                   r.mes_referencia = mes
                   r.consumo_mm = consumo_mm
                   r.tipo_comparacao = 'MM'
                   r.rec = historys.first().mm

	 	   try:
                      r.dif = (cliente.consumo_faturado - consumo_mm)/consumo_mm*100
                   except ZeroDivisionError:
                      r.dif = 0

                   if r.dif < -10.0:
                      cliente.recs.append(r)                   
                   else:
                      add = False

                   #print mes
                   #print cliente.consumo_faturado
                   #print consumo_mm
                   #print dif_intervalos
             
                # o cliente e do grupo A
             else:
                #print "cliente do grupo A"
                cliente.recs = []

                add = True
 
                for rec in recs:
                   historys = History.objects.all().filter(mm = rec).filter(date_hour__lte=rec.last_bill).filter(date_hour__gte=rec.penultimate_bill)
                   consumo_mm = 0

                   r = Rec()
                   r.mes_referencia = mes

                   for h in historys:
                      consumo_mm = consumo_mm + h.channel_1_value*1/12

                   r.consumo_mm = consumo_mm              
 
                   try:
                      r.dif = (cliente.consumo_faturado - consumo_mm)/consumo_mm*100
                   except ZeroDivisionError:
                      r.dif = 0

                   r.mm = rec.archive
                   r.constante  = rec.constant1
                   r.rec = rec

                   r.tipo_comparacao = 'REC'

                   if r.dif < -0.1:
                      cliente.recs.append(r)
                   else:
                      break

             if add == True:
                clientes.append(cliente)
                #print "ADICIONOU"

      for cliente in clientes:
         for rec in cliente.recs:
            report = RelatorioMMVersusConsumo.objects.all().filter(consumer = cliente.consumer).filter(meter=cliente.medidor).filter(mm = rec.rec)

            if len(report) == 0:
               report = RelatorioMMVersusConsumo()

               report.consumer = cliente.consumer
               report.meter = cliente.medidor
               report.consumo_faturado = cliente.consumo_faturado
               report.consumo_mm = rec.consumo_mm
               report.tipo_comparacao = rec.tipo_comparacao
               report.mes_referencia = rec.mes_referencia
               report.justificado = False
               report.mm = rec.rec
               report.company = company

               report.save()
               # only one rec of every client
            break

   fim_script = datetime.now()

   print fim_script - inicio_script


