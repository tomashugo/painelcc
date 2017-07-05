from django.core.wsgi import get_wsgi_application
from datetime import datetime, timedelta, tzinfo
import os, sys
import math

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from analysis.models import Billing, Inspection, RelatorioAlteracoesMedidor, RelatorioCorrenteZerada, RelatorioTensaoZerada, RelatorioMMVersusConsumo
   from mm.models import Consumer, Mm, Quantity, MeterHistory, History, Change 

   chars = string.letters + string.digits
   nome_arquivo = ''.join((random.choice(chars)) for x in range(20))

   if request.method == 'POST':
      form = FormBillingMM(request.POST)
   else:
      form = FormBillingMM()

   if form.is_valid():
      mes = form.cleaned_data['referencia']
   else:
      mes = datetime.strptime("01/09/16","%d/%m/%y")

   consumers = Consumer.objects.all()

   ia = Quantity.objects.get(quantity = 'Ia')
   ib = Quantity.objects.get(quantity = 'Ib')
   ic = Quantity.objects.get(quantity = 'Ic')

   class Output(object):
      pass

   class Periodo(object):
      pass

   outputs = []

   mms = History.objects.all().filter(date_hour__month = mes.month).filter(date_hour__year = mes.year).filter(channel_1_qty = ia).filter(channel_2_qty = ib).filter(channel_3_qty = ic).filter(Q(channel_1_value__gte = 7) | Q(channel_2_value__gte = 7) | Q(channel_3_value__gte = 7)).filter(~Q(mm__serial__startswith = '05')).filter(~Q(mm__serial__startswith = '03')).distinct('mm')

   mm_analisadas = []

   for mm in mms:
      history = History.objects.all().filter(mm=mm.mm).filter(date_hour__month = mes.month).filter(date_hour__year = mes.year).order_by('date_hour')
      consumer = mm.consumer

      output = Output()
      output.instalacao = consumer.installation
      output.nome = consumer.name
      output.id = consumer.id

      zerado = False

      output.periodos = []

      for h in history:
         hora = h.date_hour

         if h.channel_1_value > 7.0 or h.channel_2_value > 7.0 or h.channel_3_value > 7.0:
            if zerado == False:
               zerado = True
               a = Periodo()
               a.hora_inicio = hora
               a.ia = h.channel_1_value
               a.ib = h.channel_2_value
               a.ic = h.channel_3_value
               output.periodos.append(a)
         else:
            if zerado == True:
               zerado = False
               output.periodos[-1].hora_fim = hora
   
               dif = hora-output.periodos[-1].hora_inicio

               if dif.seconds < 3600:
                  output.periodos.pop()


      outputs.append(output)

   wb = Workbook()
   ws = wb.active

   ws.append(['Mes Referencia',mes.strftime("%d/%m/%Y")])
   ws.append(['Instalacao','Cliente','Hora Inicio','Hora Fim','Ia','Ib','Ic'])

   for output in outputs:
      for periodo in output.periodos:
         try:
            ws.append([output.instalacao,output.nome,periodo.hora_inicio,periodo.hora_fim,periodo.ia,periodo.ib,periodo.ic])
            periodo.link_mm = "?data_de="+(periodo.hora_inicio-timedelta(hours=3)).strftime("%d/%m/%Y %H:%M")+"&data_ate="+(periodo.hora_fim-timedelta(hours=3)).strftime("%d/%m/%Y %H:%M")
         except AttributeError:
            ws.append([output.instalacao,output.nome,periodo.hora_inicio," ",periodo.ia,periodo.ib,periodo.ic])	  
            data_ate = periodo.hora_inicio + timedelta(days=30)
            periodo.link_mm = "?data_de="+(periodo.hora_inicio-timedelta(hours=3)).strftime("%d/%m/%Y %H:%M")+"&data_ate="+data_ate.strftime("%d/%m/%Y %H:%M")

   xlsx = os.path.join("/home/tomash/painelcc/tmp",nome_arquivo+".xlsx")
   wb.save(xlsx)

   return render(request,'analysis/tc_saturado.html',{'outputs': outputs,'form': form,'arquivo': nome_arquivo,})

