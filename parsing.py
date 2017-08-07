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

   from analysis.models import Directory
   from django.db import models
   from crews.models import Region
   from mm.models import Consumer, Meter, MeterHistory, Mm, Quantity, EnergyFault, History, Change, Holiday, Unprocessed, Company

   UTCm3 = timedelta(hours=-3)

   class UTC(tzinfo):
      def utcoffset(self,dt):
         return UTCm3
      def dst(self,dt):
         return UTCm3
      def tzname(self,dt):
         return "UTC-3"

   utc = UTC()

   dirs = Directory.objects.all()

   for d in dirs:
      company = d.company
      nome_diretorio = d.directory
      arquivos = os.listdir(nome_diretorio)

      quantidade_arquivos = 1

      for arq in arquivos:
         # criar os threads
         # dividir as mmms

         print nome_diretorio

         if arq.find('&') == -1:
            continue

         if quantidade_arquivos > 1000:
            continue

         print arq

         caminho_arq = nome_diretorio + "/" + arq

         mm_string = ""
         for linhas in open(caminho_arq):
            mm_string = mm_string + linhas.split('\r\n')[0]

         mms = Mm.objects.filter(archive=arq)

         if len(mms) == 1:
            print "Mm ja cadastrada"
            continue

         print "Criando arquivo " + arq

         if company.name == 'Cemar':
            medidor = "33" + mm_string[0:8]
            medidor2 = "30" + mm_string[0:8]
            print medidor + " " + medidor2
            
            medidor_ = Meter.objects.filter(Q(serial__startswith=medidor) | Q(serial__startswith=medidor2))

         if company.name == 'Celpa':
            medidor = mm_string[0:8]
            medidor2 = "31" + mm_string[0:8]
            medidor_ = Meter.objects.filter(Q(serial__startswith=mm_string[0:8]) | Q(serial__startswith=medidor2))

         if len(medidor_) == 0:
            msg =  "Medidor " + medidor + " ou " + medidor2 + " Nao Encontrado"
            print msg
            print arq
            obj, created = Unprocessed.objects.get_or_create(archive=arq, msg= msg)
            continue
         else:
            medidor = medidor_.first()

         leitor = mm_string[8:14]
  
         try:
            hora_leitura = int(mm_string[14:16])
            minuto_leitura =  int(mm_string[16:18])
            segundo_leitura = int(mm_string[18:20])
            dia_leitura = int(mm_string[20:22])
            mes_leitura = int(mm_string[22:24])
            ano_leitura = 2000+int(mm_string[24:26])
            hora_ultimo_intervalo_demanda = int(mm_string[28:30])
            minuto_ultimo_intervalo_demanda = int(mm_string[30:32])
            segundo_ultimo_intervalo_demanda = int(mm_string[32:34])
            dia_ultimo_intervalo_demanda = int(mm_string[34:36])
            mes_ultimo_intervalo_demanda = int(mm_string[36:38])
            ano_ultimo_intervalo_demanda = 2000+int(mm_string[38:40])
            hora_ultima_reposicao_demanda = int(mm_string[40:42])
            minuto_ultima_reposicao_demanda = int(mm_string[42:44])
            segundo_ultima_reposicao_demanda = int(mm_string[44:46])
            dia_ultima_reposicao_demanda = int(mm_string[46:48])
            mes_ultima_reposicao_demanda = int(mm_string[48:50])
            ano_ultima_reposicao_demanda = 2000 + int(mm_string[50:52])
            hora_penultima_reposicao_demanda = int(mm_string[52:54])
            minuto_penultima_reposicao_demanda = int(mm_string[54:56])
            segundo_penultima_reposicao_demanda = int(mm_string[56:58])
            dia_penultima_reposicao_demanda = int(mm_string[58:60])
            mes_penultima_reposicao_demanda = int(mm_string[60:62])
            ano_penultima_reposicao_demanda = 2000 + int(mm_string[62:64])

            dia_hora_leitura = datetime(ano_leitura,mes_leitura,dia_leitura,hora_leitura,minuto_leitura,segundo_leitura,0,utc)
            dia_hora_ultimo_intervalo_demanda = datetime(ano_ultimo_intervalo_demanda,mes_ultimo_intervalo_demanda,dia_ultimo_intervalo_demanda,hora_ultimo_intervalo_demanda,minuto_ultimo_intervalo_demanda,segundo_ultimo_intervalo_demanda,0,utc)
            dia_hora_ultima_reposicao_demanda = datetime(ano_ultima_reposicao_demanda,mes_ultima_reposicao_demanda,dia_ultima_reposicao_demanda,hora_ultima_reposicao_demanda,minuto_ultima_reposicao_demanda,segundo_ultima_reposicao_demanda,0,utc)
            dia_hora_penultima_reposicao_demanda = datetime(ano_penultima_reposicao_demanda,mes_penultima_reposicao_demanda,dia_penultima_reposicao_demanda,hora_penultima_reposicao_demanda,minuto_penultima_reposicao_demanda,segundo_penultima_reposicao_demanda,0,utc)
         except ValueError:
            msg = "Throws Value Error Ao Processar Datas e Horas Cabecalho"
            obj, created = Unprocessed.objects.get_or_create(archive=arq, msg= msg)
            continue

         ke_medidor = mm_string[64:70] + "/" + mm_string[70:76]
         palavras_atual = int(mm_string[152:158])
         palavras_anterior = int(mm_string[158:164])
         reposicoes_demanda = int(mm_string[164:166])

         i = 170
         feriados = []
         while i < 260:
            feriado = mm_string[i:i+6]

            dia = int(feriado[0:2])
            mes = int(feriado[2:4])
            ano = 2000 + int(feriado[4:6])

            try:
               feriado = datetime(ano,mes,dia,0,0,0,0,utc)
 
               feriados.append(feriado)
            except ValueError:
               pass

            i = i + 6

         constant1 = mm_string[260:266] + "/" + mm_string[266:272]
         constant2 = mm_string[272:278] + "/" + mm_string[278:284]
         constant3 = mm_string[284:290] + "/" + mm_string[290:296]

         estado_bateria = mm_string[296:298]

         try:
            cte1 = float(mm_string[260:266])/float(mm_string[266:272])
            cte2 = float(mm_string[260:266])/float(mm_string[266:272])
            cte3 = float(mm_string[260:266])/float(mm_string[266:272])
         except ZeroDivisionError:
            msg = "Divisao Por Zero No Calculo de Constantes"
            obj, created = Unprocessed.objects.get_or_create(archive=arq, msg= msg)
            continue

         i = 0
         initial = 304

         while i < 16:
            if mm_string[initial:initial+2] != '  ':
               try:
 
                  hora_inicio_falta_energia = int(mm_string[initial:initial+2])
                  minuto_inicio_falta_energia = int(mm_string[initial+2:initial+4])
                  segundo_inicio_falta_energia = int(mm_string[initial+4:initial+6])
                  dia_inicio_falta_energia = int(mm_string[initial+6:initial+8])
                  mes_inicio_falta_energia = int(mm_string[initial+8:initial+10])
                  ano_inicio_falta_energia = 2000+int(mm_string[initial+10:initial+12])

                  hora_fim_falta_energia = int(mm_string[initial+12:initial+14])
                  minuto_fim_falta_energia = int(mm_string[initial+14:initial+16])
                  segundo_fim_falta_energia = int(mm_string[initial+16:initial+18])
                  dia_fim_falta_energia = int(mm_string[initial+18:initial+20])
                  mes_fim_falta_energia = int(mm_string[initial+20:initial+22])
                  ano_fim_falta_energia = 2000+int(mm_string[initial+22:initial+24])

                  if dia_inicio_falta_energia != 0:
                     data_hora_inicio_falta_energia = datetime(ano_inicio_falta_energia,mes_inicio_falta_energia,dia_inicio_falta_energia,hora_inicio_falta_energia,minuto_inicio_falta_energia,segundo_inicio_falta_energia,0,utc)
                     data_hora_fim_falta_energia = datetime(ano_fim_falta_energia,mes_fim_falta_energia,dia_fim_falta_energia,hora_fim_falta_energia,minuto_fim_falta_energia,segundo_fim_falta_energia,0,utc)
                     duracao_falta_energia = data_hora_fim_falta_energia - data_hora_inicio_falta_energia
                     duracao_minutos = float(duracao_falta_energia.days*1440) + float(float(duracao_falta_energia.seconds)/60)
               except ValueError:
                  pass
            initial = initial + 24
            i = i + 1

         i = 0
         initial = 1906

         while i < 16:
            print "."
            try: 
               codigo_alteracao = str(mm_string[initial:initial+2])
               leitor_alteracao = str(mm_string[initial+2:initial+8])
               hora_alteracao = int(mm_string[initial+8:initial+10])
               minuto_alteracao = int(mm_string[initial+10:initial+12])
               segundo_alteracao = int(mm_string[initial+12:initial+14])
               dia_alteracao = int(mm_string[initial+14:initial+16])
               mes_alteracao = int(mm_string[initial+16:initial+18])
               ano_alteracao = 2000 + int(mm_string[initial+18:initial+20])

               alteracao = datetime(ano_alteracao,mes_alteracao,dia_alteracao,hora_alteracao,minuto_alteracao,segundo_alteracao,0,utc)
               obj, created = Change.objects.get_or_create(code=codigo_alteracao,observation=code_alteracao[int(codigo_alteracao)],meter=medidor_.first(),leitor=leitor_alteracao,date_time=alteracao)
               if created:
                  obj.save()
                  print "# change inserted"
            except ValueError:
               i = 17
               msg = "ValueError Ao Criar Objeto Change"
               obj, created = Unprocessed.objects.get_or_create(archive=arq, msg= msg)
               continue        
            except KeyError:
               i = 17
               msg = "KeyError Ao Criar Objeto Change"
               obj, created = Unprocessed.objects.get_or_create(archive=arq, msg= msg)
               continue
            except MultipleObjectsReturned:
               i = 17
               msg = "MultipleObjectsReturned Ao Criar Objeto Change"
               obj, created = Unprocessed.objects.get_or_create(archive=arq, msg= msg)
               continue

            initial = initial + 20
            i = i + 1

         modelo_medidor = mm_string[2304:2308]
         versao_software = mm_string[298:302]
         grandeza_canal_1 = mm_string[2308:2310]
         grandeza_canal_2 = mm_string[2310:2312]
         grandeza_canal_3 = mm_string[2312:2314]

         # primeira condicao SAGA 1000 - 3304
         # segunda condicao  SAGA 1500 - 3305

         if constant1 == "000001/002000" or constant1 == "000001/000048" or constant1 == "000001/001750":
            grandeza_canal_1 = "17"
            grandeza_canal_2 = "18"
            grandeza_canal_3 = "19"
      
         if constant1 == "000001/000080" or constant1 == "000001/000024":
            grandeza_canal_1 = "20"
            grandeza_canal_2 = "21"
            grandeza_canal_3 = "22"

         grandeza_canal_1_ = Quantity.objects.filter(code=grandeza_canal_1)
         grandeza_canal_2_ = Quantity.objects.filter(code=grandeza_canal_2)
         grandeza_canal_3_ = Quantity.objects.filter(code=grandeza_canal_3)

         if len(grandeza_canal_1_) == 0:
            msg = "Grandeza Desconhecida Canal 1 " + grandeza_canal_1
            obj, created = Unprocessed.objects.get_or_create(archive=arq, msg= msg) 
            continue
         else:
            grandeza_canal_1 = grandeza_canal_1_.first()

         if len(grandeza_canal_2_) == 0:
            msg = "Grandeza Desconhecida Canal 2 " + grandeza_canal_2
            obj, created = Unprocessed.objects.get_or_create(archive=arq, msg= msg) 
            continue
         else:
            grandeza_canal_2 = grandeza_canal_2_.first()

         if len(grandeza_canal_3_) == 0:
            msg = "Grandeza Desconhecida Canal 3 " + grandeza_canal_3
            obj, created = Unprocessed.objects.get_or_create(archive=arq, msg= msg) 
            continue
         else:
            grandeza_canal_3 = grandeza_canal_3_.first()

         try:
            arq_publico, created = Mm.objects.get_or_create(company=company,archive=arq,date_hour=dia_hora_leitura,path=caminho_arq,reader=leitor,serial=mm_string[0:8],model=modelo_medidor,version=versao_software,constant1=constant1,constant2=constant2,constant3=constant3,channel_1_qty=grandeza_canal_1,channel_2_qty=grandeza_canal_2,channel_3_qty=grandeza_canal_3,last_integration=dia_hora_ultimo_intervalo_demanda,last_bill=dia_hora_ultima_reposicao_demanda,penultimate_bill=dia_hora_penultima_reposicao_demanda,meter_object=medidor,status_batery=estado_bateria)
         except MultipleObjectsReturned:
            msg = "MultipleObjectsReturned Ao Criar Objeto MM"
            obj, created = Unprocessed.objects.get_or_create(archive=arq, msg= msg) 
            continue

         if created:
            arq_publico.save()
         else:
            continue

         if created:
            quantidade_arquivos = quantidade_arquivos+1

         for i in feriados:
            a = Holiday()
            a.holiday = i
            a.mm = arq_publico
            a.save()

         initial = 2400

         meter_history = medidor.meterhistory.filter(since__lte = dia_hora_leitura).filter(until__gte = dia_hora_leitura)

         if len(meter_history) > 0:
            consumer = meter_history.first().consumer
            print dia_hora_leitura
            primeiro_intervalo = dia_hora_ultimo_intervalo_demanda - timedelta(minutes=max([palavras_anterior,palavras_atual])/3*5-5)
            print consumer
            print primeiro_intervalo
            while initial < len(mm_string):
               initial = initial+12
               for i in range(0,24):
                  if mm_string[initial+i*12:initial+i*12+4] != "    ":	          
                     pulse1 = mm_string[initial+i*12:initial+i*12+4]
                     pulse2 = mm_string[initial+i*12+4:initial+i*12+8]
                     pulse3 = mm_string[initial+i*12+8:initial+i*12+12]
                  
                     if float(pulse1) < 2048:
                        pulse1 = float(pulse1)
                     else:
                        pulse1 = 2048 - float(pulse1)

                     if float(pulse2) < 2048:
                        pulse2 = float(pulse2)
                     else:
                        pulse2 = 2048 - float(pulse2)

                     if float(pulse3) < 2048:
                        pulse3 = float(pulse3)
                     else:
                        pulse3 = 2048 - float(pulse3)
                  
                     value1 = cte1*pulse1*12
                     value2 = cte2*pulse2*12
                     value3 = cte3*pulse3*12

                     history = History(consumer=consumer,date_hour=primeiro_intervalo,channel_1_value=value1,channel_2_value=value2,channel_3_value=value3,channel_1_qty=grandeza_canal_1,channel_2_qty=grandeza_canal_2,channel_3_qty=grandeza_canal_3,channel_1_pulse=pulse1,channel_2_pulse=pulse2,channel_3_pulse=pulse3,mm=arq_publico)
                     #print "\t" + str(pulse1) + "\t" + str(value1) + "\t" + str(pulse2) + "\t" + str(value2) + "\t" + str(pulse3) + "\t" + str(value3)   
                     primeiro_intervalo = primeiro_intervalo + timedelta(minutes=5)
                     history.save()
               initial = initial + 288
