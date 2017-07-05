from django.shortcuts import render
from .forms import ProducaoForm, AlvosAbertos
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import string, random, os
from openpyxl import Workbook
from .models import AlvosAbertos, AlvosDespachados, Producao
from mm.models import Company, MeterHistory
from analysis.models import Inspection
from .forms import AlvosAbertosForm, ReceberAlvoForm
from crews.models import Employee
# Create your views here.

def index(request):
   message = request.GET.get('message')

   if request.method == 'POST':
      form = ProducaoForm(request.POST)
      if form.is_valid():              
       
         post = form.save(commit=False)
         post.envio = datetime.datetime.now()
	 post.save()

         return HttpResponseRedirect('/producao/?message=sucesso')
   else:
      form = ProducaoForm()

   return render(request,'producao/form.html',{'message':message,'form':form,})

@login_required(login_url='/admin/login/')
def form_receber_alvo(request):
   company_session = Company.objects.get(name=request.session['Company'])

   if request.method == 'GET':
      form = ReceberAlvoForm()
      id = request.GET.get('id')

      alvo = Producao.objects.get(id=id) 

      #versao = request.GET.get('versao')

      versao = '2.0'

      if versao == '2.0':
         return render(request,'producao/form_receber_alvov2.0.html',{'form' : form,'alvo':alvo,'company_session':company_session,})
      else:
         return render(request,'producao/form_receber_alvo.html',{'form' : form,'alvo':alvo,})

   else:
      form = ReceberAlvoForm(request.POST)
      if form.is_valid():
         id = request.GET.get('id')
         prod = Producao.objects.get(id=id)
         prod.data_devolucao = form.cleaned_data['data_devolucao']
         prod.save()
      
         return HttpResponseRedirect('/analysis/producao/?message=sucesso')


@login_required(login_url='/admin/login/')
def form_alvos_abertos(request):
   company_session = Company.objects.get(name=request.session['Company'])

   if request.method == 'GET':
      form = AlvosAbertosForm()
      id = request.GET.get('id')

      alvo = AlvosAbertos.objects.get(id=id) 

      #versao = request.GET.get('versao')

      versao = '2.0'

      if versao == '2.0':
         return render(request,'producao/form_alvos_abertosv2.0.html',{'alvo':alvo,'form' : form,'company_session':company_session,})
      else:
         return render(request,'producao/form_alvos_abertos.html',{'alvo':alvo,'form' : form,})

   else:
      form = AlvosAbertosForm(request.POST)
      if form.is_valid():
         id = request.GET.get('id')
         alvo = AlvosDespachados()
         alvo.inspetor = form.cleaned_data['inspetor']
         alvo.data_despacho = form.cleaned_data['data_despacho']
         alvo.alvo_aberto = AlvosAbertos.objects.get(id=id)
         alvo.save()
         return HttpResponseRedirect('/producao/alvos_abertos/?message=sucesso')
      return HttpResponse("Algo deu errado")


@login_required(login_url='/admin/login/')
def alvos_abertos(request):
   company_session = Company.objects.get(name=request.session['Company'])
   chars = string.letters + string.digits
   nome_arquivo = ''.join((random.choice(chars)) for x in range(20))

   class Output(object):
      pass

   class Periodo(object):
      pass

   outputs = []

   alarms = AlvosAbertos.objects.all()

   message = request.GET.get('message')
   #versao = request.GET.get('versao')
   versao = '2.0'

   for alarm in alarms:
      output = Output()

      output.id = alarm.id
      output.data_geracao = alarm.data_geracao
      output.consumer = alarm.consumer
      output.observacao = alarm.observacao
      output.ns = alarm.ns

      hoje = datetime.datetime.now()

      meter = MeterHistory.objects.all().filter(consumer=alarm.consumer).filter(since__lte=hoje).filter(until__gte=hoje)

      try:
         output.serial = meter.first().meter.serial
      except AttributeError:
         pass

      despachados = AlvosDespachados.objects.all().filter(alvo_aberto = alarm)
      executados = Producao.objects.all().filter(data_realizacao__gte=alarm.data_geracao).filter(instalacao=output.consumer.installation)
      
      output.executado = False

      if len(executados) > 0:
         output.executado = True

      if len(despachados) == 0:
         outputs.append(output)

   wb = Workbook()
   ws = wb.active

   ws.append(['Ns','Data Geracao','Instalacao','Medidor','Cliente','Localidade','Regional','Observacao'])

   for output in outputs:
      try:
         serial = output.serial
      except AttributeError:
         serial = ""

      ws.append([output.ns,output.data_geracao,output.consumer.installation,serial,output.consumer.name,output.consumer.city,output.consumer.region.name,output.observacao])

   xlsx = os.path.join("/home/tomash/painelcc/tmp",nome_arquivo+".xlsx")
   wb.save(xlsx)
 
   if versao == '2.0':
      return render(request,'producao/alvos_abertosv2.0.html',{'message':message,'company_session':company_session,'outputs': outputs,'arquivo': nome_arquivo,})
   else:
      return render(request,'producao/alvos_abertos.html',{'message':message,'company_session':company_session,'outputs': outputs,'arquivo': nome_arquivo,})


@login_required(login_url='/admin/login/')
def alvos_despachados(request):
   company_session = Company.objects.get(name=request.session['Company'])
   chars = string.letters + string.digits
   nome_arquivo = ''.join((random.choice(chars)) for x in range(20))

   class Output(object):
      pass

   class Periodo(object):
      pass

   outputs = []

   alarms = AlvosDespachados.objects.all().order_by('-alvo_aberto','-data_despacho')

   id_anterior = 0

   wb = Workbook()
   ws = wb.active

   ws.append(['Ns','Data Geracao','Instalacao','Cliente','Regional','Observacao','Data Despacho','Data Executado','Tempo Execucao','Inspetor'])

   for alarm in alarms:
      output = Output()

      if id_anterior != alarm.alvo_aberto.id:
         output.data_geracao = alarm.alvo_aberto.data_geracao
         output.observacao = alarm.alvo_aberto.observacao
         output.ns = alarm.alvo_aberto.ns  
         output.installation = alarm.alvo_aberto.consumer.installation
         output.name = alarm.alvo_aberto.consumer.name
         output.region = alarm.alvo_aberto.consumer.region.name     
      else:
         output.installation = ""
         output.name = ""
         output.data_geracao = ""
         output.observacao = ""
         output.ns = ""
         output.region = ""


      id_anterior = alarm.alvo_aberto.id

      output.data_despacho = alarm.data_despacho
      output.id = alarm.alvo_aberto.id
      output.inspetor = alarm.inspetor

      executado = Inspection.objects.all().filter(ns=alarm.alvo_aberto.ns)
      
      if len(executado) > 0:
         output.data_executado = executado.first().date_time_executed
      else:
         output.data_executado = ""
      
      if output.data_executado != "":
         ws.append([alarm.alvo_aberto.ns,alarm.alvo_aberto.data_geracao,alarm.alvo_aberto.consumer.installation,alarm.alvo_aberto.consumer.name,alarm.alvo_aberto.consumer.region.name,alarm.alvo_aberto.observacao,alarm.data_despacho,output.data_executado,(output.data_executado.date()-alarm.data_despacho).days,unicode(alarm.inspetor)])
      else:
         ws.append([alarm.alvo_aberto.ns,alarm.alvo_aberto.data_geracao,alarm.alvo_aberto.consumer.installation,alarm.alvo_aberto.consumer.name,alarm.alvo_aberto.consumer.region.name,alarm.alvo_aberto.observacao,alarm.data_despacho,output.data_executado,"",unicode(alarm.inspetor)])


      outputs.append(output)


   xlsx = os.path.join("/home/tomash/painelcc/tmp",nome_arquivo+".xlsx")
   wb.save(xlsx)

   #versao = request.GET.get('versao')
   versao = '2.0'

   if versao == '2.0':
      return render(request,'producao/alvos_despachadosv2.0.html',{'company_session':company_session,'outputs': outputs,'arquivo': nome_arquivo,})
   else:
      return render(request,'producao/alvos_despachados.html',{'company_session':company_session,'outputs': outputs,'arquivo': nome_arquivo,})


@login_required(login_url='/admin/login/')
def stats(request):
   company_session = Company.objects.get(name=request.session['Company'])

   class Output(object):
      pass

   class Periodo(object):
      pass

   outputs = []

   alarms = AlvosDespachados.objects.all().order_by('-alvo_aberto','-data_despacho')

   hoje = datetime.datetime.now()

   tempo_medio = dict()

   for i in Employee.objects.all():
      tempo_medio[i] = []

   for alarm in alarms:
      diff = hoje.date()-alarm.data_despacho
      inspecoes = Inspection.objects.all().filter(ns = alarm.alvo_aberto.ns)

      if len(inspecoes) == 0:
         tempo_medio[alarm.inspetor].append(diff.days)

   a = ""

   outputs = []

   for keyvalue in tempo_medio.items():
      if len(tempo_medio[keyvalue[0]]) != 0:
         media = str(sum(tempo_medio[keyvalue[0]])/len(tempo_medio[keyvalue[0]])) + " dias"
         quantidade = str(len(tempo_medio[keyvalue[0]])) + " alvos"
         maior = str(max(tempo_medio[keyvalue[0]])) + " dias"

         output = Output()
         output.inspetor = str(keyvalue[0])
         output.media = media
         output.quantidade = quantidade
         output.maior = maior
      
         outputs.append(output)

   #return HttpResponse(a)

   return render(request,'producao/stats.html',{'company_session':company_session,'outputs': outputs,})

@login_required(login_url='/admin/login/')
def alvos_nao_baixados(request):
   company_session = Company.objects.get(name=request.session['Company'])
   chars = string.letters + string.digits
   nome_arquivo = ''.join((random.choice(chars)) for x in range(20))

   class Output(object):
      pass

   class Periodo(object):
      pass

   outputs = []

   producoes = Producao.objects.all().filter(tipo_servico__id = 14)

   for p in producoes:
      output = Output()

      alvo_aberto = AlvosAbertos.objects.all().filter(data_geracao__lte = p.data_realizacao).filter(consumer__installation = p.instalacao)

      if len(alvo_aberto) == 1:
         alvo_aberto = alvo_aberto.first()

         inspection = Inspection.objects.all().filter(ns = alvo_aberto.ns)

         if len(inspection) == 0:
            output.data_geracao = alvo_aberto.data_geracao
            output.consumer = alvo_aberto.consumer
            output.observacao = alvo_aberto.observacao
            output.ns = alvo_aberto.ns
            output.inspetor = p.tecnico
            output.data_realizacao = p.data_realizacao
            output.diferenca = datetime.datetime.now().date() - output.data_realizacao

            outputs.append(output)

   wb = Workbook()
   ws = wb.active

   ws.append(['Ns','Data Geracao','Instalacao','Cliente','Observacao','Data Realizacao','Inspetor','Diferenca'])

   for output in outputs:
      ws.append([output.ns,output.data_geracao,output.consumer.installation,output.consumer.name,output.observacao,output.data_realizacao,unicode(output.inspetor),output.diferenca])

   xlsx = os.path.join("/home/tomash/painelcc/tmp",nome_arquivo+".xlsx")
   wb.save(xlsx)

   #versao = request.GET.get('versao')

   versao = '2.0'

   if versao == '2.0':
      return render(request,'producao/alvos_nao_baixadosv2.0.html',{'company_session':company_session,'outputs': outputs,'arquivo': nome_arquivo,})
   else:
      return render(request,'producao/alvos_nao_baixados.html',{'company_session':company_session,'outputs': outputs,'arquivo': nome_arquivo,})
