from datetime import tzinfo, timedelta,datetime
import os

UTCm3 = timedelta(hours=-3)

class UTC(tzinfo):
   def dst(self,dt):
      return UTCm3
   def tzname(self,dt):
      return "UTC-3"

utc = UTC()

nome_diretorio = "upload/mm"
arquivos = os.listdir(nome_diretorio)

for arq in arquivos:
   print arq

   caminho_arq = nome_diretorio + "/" + arq
   
   mm_string = ""
   for linhas in open(caminho_arq):
      mm_string = mm_string + linhas.split('\r\n')[0]


   medidor = "33" + mm_string[0:8]
   leitor = mm_string[8:14]

   #print "\t33" + mm_string[0:8] # medidor
   #print "\t" + mm_string[8:14] # leitor
   hora_leitura = int(mm_string[14:16])
   minuto_leitura =  int(mm_string[16:18])
   segundo_leitura = int(mm_string[18:20])
   dia_leitura = int(mm_string[20:22])
   mes_leitura = int(mm_string[22:24])
   ano_leitura = 2000+int(mm_string[32:34])
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

   #print "\t" + mm_string[14:16] + ":" + mm_string[16:18] + ":" + mm_string[18:20] # hora_leitura
   #print "\t" + mm_string[20:22] + "/" + mm_string[22:24] + "/20" + mm_string[24:26] # dia_leitura
   #print "\t" + mm_string[28:30] + ":" + mm_string[30:32] + ":" + mm_string[32:34] # hora_ultimo_intervalo_demanda
   #print "\t" + mm_string[34:36] + "/" + mm_string[36:38] + "/" + mm_string[38:40] # data_ultimo_intervalo_demanda
   #print "\t" + mm_string[40:42] + ":" + mm_string[42:44] + ":" + mm_string[44:46] # hora_ultima_reposicao_demanda
   #print "\t" + mm_string[46:48] + "/" + mm_string[48:50] + "/20" + mm_string[50:52] # data_ultima_reposicao_demanda
   #print "\t" + mm_string[52:54] + ":" + mm_string[54:56] + ":" + mm_string[56:58] # hora_penultima_reposicao_demanda
   #print "\t" + mm_string[58:60] + "/" + mm_string[60:62] + "/20" + mm_string[62:64] # data_penultima_reposicao_demanda
   print "\t" + mm_string[64:70] + "/" + mm_string[70:76] # ke medidor  
   print "\t" + mm_string[152:158] # numero de palavras atual
   print "\t" + mm_string[158:164] # numero de palavras anterior
   print "\t" + mm_string[164:166] # numero de reposicoes de demanda
   print "\t" + mm_string[170:176] # feriado 1
   print "\t" + mm_string[176:182] # feriado 2
   print "\t" + mm_string[182:188] # feriado 3
   print "\t" + mm_string[188:194] # feriado 4
   print "\t" + mm_string[194:200] # feriado 5
   print "\t" + mm_string[200:206] # feriado 6
   print "\t" + mm_string[206:212] # feriado 7
   print "\t" + mm_string[212:218] # feriado 8
   print "\t" + mm_string[218:224] # feriado 9
   print "\t" + mm_string[224:230] # feriado 10
   print "\t" + mm_string[230:236] # feriado 11
   print "\t" + mm_string[236:242] # feriado 12
   print "\t" + mm_string[242:248] # feriado 13
   print "\t" + mm_string[248:254] # feriado 14
   print "\t" + mm_string[254:260] # feriado 15
   print "\t" + mm_string[260:266] + "/" + mm_string[266:272] # constante canal 1
   print "\t" + mm_string[272:278] + "/" + mm_string[278:284] # constante canal 2
   print "\t" + mm_string[284:290] + "/" + mm_string[290:296] # constante canal 3
   print "\t" + mm_string[296:298] # estado da bateria

   cte1 = float(mm_string[260:266])/float(mm_string[266:272])
   cte2 = float(mm_string[260:266])/float(mm_string[266:272])
   cte3 = float(mm_string[260:266])/float(mm_string[266:272])

   i = 0
   initial = 304

   while i < 16:
      print "\t" + "Falta de Energia " + str(i+1)
      print "\t" + mm_string[initial:initial+2] + ":" + mm_string[initial+2:initial+4] + ":" + mm_string[initial+4:initial+6] # hora inicio da falta de energia 
      print "\t" + mm_string[initial+6:initial+8] + "/" + mm_string[initial+8:initial+10] + "/20" + mm_string[initial+10:initial+12] # dia inicio da falta de energia 
      print "\t" + mm_string[initial+12:initial+14] + ":" + mm_string[initial+14:initial+16] + ":" + mm_string[initial+16:initial+18] # hora fim da falta de energia 
      print "\t" + mm_string[initial+18:initial+20] + "/" + mm_string[initial+20:initial+22] + "/20" + mm_string[initial+22:initial+24] # dia fim da falta de energia 

      i = i + 1
      initial = initial + 24

   i = 0
   initial = 1906

   while i < 16:
      print "\t" + "Alteracao Numero " + str(i+1)
      print "\t" + mm_string[initial:initial+2] + "\t" + mm_string[initial+2:initial+8] + "\t" + mm_string[initial+8:initial+10] + ":" + mm_string[initial+10:initial+12] + ":" + mm_string[initial+12:initial+14] + "\t" + mm_string[initial+14:initial+16] + "/" + mm_string[initial+16:initial+18] + "/20" + mm_string[initial+18:initial+20]
      initial = initial + 20
      i = i + 1

   print "\t" + mm_string[2304:2308] # modelo do medidor
   print "\t" + mm_string[298:302]   # versao do softwares
   print "\t" + mm_string[2308:2310] # grandeza canal 1
   print "\t" + mm_string[2310:2312] # grandeza canal 2
   print "\t" + mm_string[2312:2314] # grandeza canal 3

   initial = 2400

   while initial < len(mm_string):
      initial = initial+12
      for i in range(0,24):
         if mm_string[initial+i*12:initial+i*12+4] != "    ":
            pulse1 = mm_string[initial+i*12:initial+i*12+4]
            pulse2 = mm_string[initial+i*12+4:initial+i*12+8]
            pulse3 = mm_string[initial+i*12+8:initial+i*12+12]
            value1 = cte1*float(pulse1)*12
            value2 = cte2*float(pulse2)*12
            value3 = cte3*float(pulse3)*12
            print "\t" + str(pulse1) + "\t" + str(value1) + "\t" + str(pulse2) + "\t" + str(value2) + "\t" + str(pulse3) + "\t" + str(value3)

      initial = initial + 288
