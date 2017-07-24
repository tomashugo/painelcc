from django.http import HttpResponse
from django.template import loader
from mm.models import Consumer, Quantity
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import timedelta
from datetime import datetime
from analysis.models import RelatorioMMVersusConsumo, RelatorioAlteracoesMedidor, RelatorioCorrenteZerada, RelatorioTensaoZerada, RelatorioQuedaDeConsumo, Billing, Inspection, RelatorioFraudeNaoIncrementada
from mm.models import Mm, MeterHistory, Company
from django.db.models import Q

from .forms import FormMM

@login_required(login_url='/admin/login/')
def index(request):
   company_session = Company.objects.get(name=request.session['Company'])
   
   quantidade_fraude_nao_incrementada = len(RelatorioFraudeNaoIncrementada.objects.all().filter(justificado=False).filter(company=company_session).filter(company=company_session))
   quantidade_queda_consumo = len(RelatorioQuedaDeConsumo.objects.all().filter(justificado = False).filter(company=company_session).distinct('consumer'))
   quantidade_relatorio_mm_versus_consumo = len(RelatorioMMVersusConsumo.objects.all().filter(justificado = False).filter(company=company_session))
   quantidade_alteracoes_medidor = len(RelatorioAlteracoesMedidor.objects.all().filter(justificado = False).distinct('consumer').distinct('data_alteracao').filter(company=company_session))

   justificado_fraude_nao_incrementada = len(RelatorioFraudeNaoIncrementada.objects.all().filter(justificado=True))
   justificado_relatorio_mm_versus_consumo = len(RelatorioMMVersusConsumo.objects.all().filter(justificado = True).filter(company=company_session))
   justificado_alteracoes_medidor = len(RelatorioAlteracoesMedidor.objects.all().filter(justificado = True).distinct('consumer').distinct('data_alteracao').filter(company=company_session))
   justificado_queda_consumo = len(RelatorioQuedaDeConsumo.objects.all().filter(justificado = True).filter(company=company_session))

   quantidade_corrente_zerada = len(RelatorioCorrenteZerada.objects.all().filter(justificado = False).distinct('consumer').filter(company=company_session))
   justificado_corrente_zerada = len(RelatorioCorrenteZerada.objects.all().filter(justificado = True).distinct('consumer').filter(company=company_session))

   quantidade_tensao_zerada = len(RelatorioTensaoZerada.objects.all().filter(justificado = False).distinct('consumer').filter(company=company_session))
   justificado_tensao_zerada = len(RelatorioTensaoZerada.objects.all().filter(justificado = True).distinct('consumer').filter(company=company_session))

   quantidade_mm = len(Mm.objects.all().filter(company=company_session))

   nao_justificados = quantidade_relatorio_mm_versus_consumo + quantidade_alteracoes_medidor + quantidade_corrente_zerada + quantidade_tensao_zerada + quantidade_queda_consumo + quantidade_fraude_nao_incrementada
   justificados = justificado_relatorio_mm_versus_consumo + justificado_alteracoes_medidor + justificado_corrente_zerada + justificado_tensao_zerada + justificado_queda_consumo
 
   #versao = request.GET.get('versao')
   versao = '2.0'

   gerado_fraude_nao_incrementada = len(RelatorioFraudeNaoIncrementada.objects.all().filter(justificado=True).filter(company=company_session).filter(alvo_gerado=True))
   gerado_relatorio_mm_versus_consumo = len(RelatorioMMVersusConsumo.objects.all().filter(justificado = True).filter(company=company_session).filter(alvo_gerado=True))
   gerado_alteracoes_medidor = len(RelatorioAlteracoesMedidor.objects.all().filter(justificado = True).distinct('consumer').distinct('data_alteracao').filter(company=company_session).filter(alvo_gerado=True))
   gerado_queda_consumo = len(RelatorioQuedaDeConsumo.objects.all().filter(justificado = True).filter(company=company_session).filter(alvo_gerado=True))
   gerado_corrente_zerada = len(RelatorioCorrenteZerada.objects.all().filter(justificado = True).distinct('consumer').filter(company=company_session).filter(alvo_gerado=True))
   gerado_tensao_zerada = len(RelatorioTensaoZerada.objects.all().filter(justificado = True).distinct('consumer').filter(company=company_session).filter(alvo_gerado=True))
   
   alvos_gerados = gerado_fraude_nao_incrementada + gerado_relatorio_mm_versus_consumo + gerado_alteracoes_medidor + gerado_queda_consumo + gerado_corrente_zerada + gerado_tensao_zerada


   hoje = datetime.now()

   if hoje.month < 10:
      mes = "0" + str(hoje.month)
   else:
      mes = str(hoje.month)

   mes = "01/" + str(mes) + "/" + str(hoje.year)

   if versao == "2.0":
      context =  { 'justificado_fraude_nao_incrementada' : justificado_fraude_nao_incrementada, 'quantidade_fraude_nao_incrementada' : quantidade_fraude_nao_incrementada, 'company_session': company_session, 'quantidade_relatorio_mm_versus_consumo' : quantidade_relatorio_mm_versus_consumo, 'quantidade_alteracoes_medidor': quantidade_alteracoes_medidor, 'quantidade_mm' : quantidade_mm, 'nao_justificados' : nao_justificados, 'justificados' : justificados, 'quantidade_corrente_zerada' : quantidade_corrente_zerada, 'justificado_corrente_zerada' : justificado_corrente_zerada,'quantidade_tensao_zerada':quantidade_tensao_zerada,'justificado_tensao_zerada':justificado_tensao_zerada, 'quantidade_queda_consumo' : quantidade_queda_consumo,'mes':mes,'alvos_gerados':alvos_gerados,'host': request.META['HTTP_HOST'],}
      template = loader.get_template('indexv2.0.html')
   else:
      context =  { 'justificado_fraude_nao_incrementada' : justificado_fraude_nao_incrementada, 'quantidade_fraude_nao_incrementada' : quantidade_fraude_nao_incrementada, 'company_session': company_session, 'quantidade_relatorio_mm_versus_consumo' : quantidade_relatorio_mm_versus_consumo, 'quantidade_alteracoes_medidor': quantidade_alteracoes_medidor, 'quantidade_mm' : quantidade_mm, 'nao_justificados' : nao_justificados, 'justificados' : justificados, 'quantidade_corrente_zerada' : quantidade_corrente_zerada, 'justificado_corrente_zerada' : justificado_corrente_zerada,'quantidade_tensao_zerada':quantidade_tensao_zerada,'justificado_tensao_zerada':justificado_tensao_zerada, 'quantidade_queda_consumo' : quantidade_queda_consumo,'mes':mes,}
      template = loader.get_template('index.html')
   return HttpResponse(template.render(context,request))

@login_required(login_url='/admin/login/')
def revenue_match(request):
   company_session = Company.objects.get(name=request.session['Company'])

   context =  { }
   template = loader.get_template('revenue.html')
   return HttpResponse(template.render(context,request))


def csrf_failure(request,reason):
   context =  { }
   template = loader.get_template('403CSRF.html')
   return HttpResponse(template.render(context,request))


@login_required(login_url='/admin/login/')
def consumer(request):
   company_session = Company.objects.get(name=request.session['Company'])

   if request.method == 'POST':
      query = request.POST.get('q')
   else:
      query = request.GET.get('q')

   #versao = request.GET.get('versao')

   if query == None:
      query = ""
  
   latest_consumer_list = Consumer.objects.filter(Q(installation__contains = query) | Q(name__icontains = query)).filter(company=company_session)

   paginator = Paginator(latest_consumer_list,200)

   page = request.GET.get('page')

   if page is None:
      page = 1

   try:
      latest_consumer_list = paginator.page(page)
   except PageNotAnInteger:
      latest_consumer_list = paginator.page(1)
   except EmptyPage:
      latest_consumer_list = paginator.page(paginator.num_pages)

   paginas = []

   num_pages = paginator.num_pages

   a = range(1,num_pages)
  
   for i in a:
      paginas.append(i)
   
   try:
      while paginas[0] < int(page) - 2:
         paginas.pop(0)
   except IndexError:
      pass

   add = 0
  
   try:
      if int(page) - paginas[0] < 2:
         add = 2 - (int(page) - paginas[0])
   except IndexError:
      pass

   try:
      while paginas[-1] > int(page) + 2 + add:
         paginas.pop()
   except IndexError:
      pass
  
  
   versao = '2.0'
   
   if versao == '2.0':
      context = { 'company_session': company_session, 'latest_consumer_list' : latest_consumer_list,'query':query,'paginas':paginas,'page':int(page),'query':query, }
      template = loader.get_template('consumerv2.0.html')
   else:
      context = { 'company_session': company_session, 'latest_consumer_list' : latest_consumer_list,'query':query, }
      template = loader.get_template('consumer.html')

   return HttpResponse(template.render(context,request))

@login_required(login_url='/admin/login/')
def consumer_detail(request,consumer_id):
   company_session = Company.objects.get(name=request.session['Company'])

   consumer = Consumer.objects.get(id=consumer_id)
   #channel1_qty = Quantity.objects.get(quantity='kW')
   #channel2_qty = Quantity.objects.get(quantity='kVarI')
   #channel3_qty = Quantity.objects.get(quantity='kVarC')

   #history = consumer.history_set.all().filter(channel_1_qty=channel1_qty).filter(channel_2_qty=channel2_qty).filter(channel_3_qty=channel3_qty).order_by('date_hour')[:1440]
   inspections = consumer.inspection_set.all().order_by('-date_time_executed')
   """
   for i in inspections:
      date_time_executed = i.date_time_executed
      try:
         meter = MeterHistory.objects.all().filter(consumer=consumer).filter(since__lte = date_time_executed).filter(until__gte = date_time_executed).first().meter
         mms = Mm.objects.all().filter(meter_object=meter).filter(date_hour__day = date_time_executed.day).filter(date_hour__month = date_time_executed.month).filter(date_hour__year = date_time_executed.year)

         i.mms = []

         for mm in mms:
            i.mms.append(mm)
      except AttributeError:
         pass
   """
   meterhistory=consumer.meterhistory_set.all()
   mms=[]
   for i in meterhistory:
     meter = i.meter
     lista = Mm.objects.all().filter(meter_object=meter).filter(date_hour__gte=i.since).filter(date_hour__lt=i.until)
     for l in lista:
         mms.append(l)
            
            
            
   class Grafico(object):
      pass

   class Alarmes(object):
      pass

   meses = []

   inicio = datetime.strptime("01/01/2014","%d/%m/%Y")
   agora  = datetime.now()
   #agora = datetime.strptime("01/07/2016","%d/%m/%Y")

   while inicio.month != agora.month or inicio.year != agora.year:
      meses.append(inicio)

      if inicio.month == 12:
         inicio = inicio.replace(month = 1)
         inicio = inicio.replace(year = inicio.year + 1)
      else:
         inicio = inicio.replace(month = inicio.month + 1)

   grafico = []

   meses.append(agora.replace(day = 1))

   for mes in meses:
      billings = Billing.objects.all().filter(consumer=consumer).filter(reference = mes)
      faturado = 0

      entrou = False

      for bill in billings:
         faturado = faturado+bill.billed   
         entrou = True
   
      g = Grafico()

      observacao = []
      
      inspecoes = Inspection.objects.all().filter(consumer=consumer).filter(date_time_executed__year = mes.year).filter(date_time_executed__month = mes.month)
      alteracoes_medidor = RelatorioAlteracoesMedidor.objects.all().filter(consumer=consumer).filter(data_alteracao__month = mes.month).filter(data_alteracao__year = mes.year)
      corrente_zerada = RelatorioCorrenteZerada.objects.all().filter(consumer=consumer).filter(inicio__month = mes.month).filter(inicio__year = mes.year)
      tensao_zerada = RelatorioTensaoZerada.objects.all().filter(consumer=consumer).filter(inicio__month = mes.month).filter(inicio__year = mes.year)
      troca_medidor = MeterHistory.objects.all().filter(consumer=consumer).filter(since__month = mes.month).filter(since__year = mes.year)      

      if len(troca_medidor) > 0:
         observacao.append("Troca de Medidor")

      if len(alteracoes_medidor) > 0:
         alt = alteracoes_medidor.first()
 
         if alt.justificado:
            observacao.append("Alteracoes Medidor: " + alt.observacao + " JUSTIFICADO")
         else:
            observacao.append("Alteracoes Medidor: " + alt.observacao + " N JUSTIFICADO")

      if len(corrente_zerada) > 0:
         c = corrente_zerada.first()

         if c.justificado:
            observacao.append("Corrente Zerada" + " JUSTIFICADO")
         else:
            observacao.append("Corrente Zerada" + " N JUSTIFICADO")

      if len(tensao_zerada) > 0:
         c = tensao_zerada.first()

         if c.justificado:
            observacao.append("Tensao Zerada" + " JUSTIFICADO")
         else:
            observacao.append("Tensao Zerada" + " N JUSTIFICADO")

      if len(inspecoes) > 0:
         for insp in inspecoes:
            observacao.append("Inspecao Cod " + insp.code)

      try:      
         g.dia = billings.first().end_cycle.day
      except AttributeError:
         g.dia = 1         

      g.mes = mes.month - 1
      g.ano = mes.year
      g.consumo = faturado
   
      if len(observacao) > 0:
         g.observacao = ", ".join(observacao)

      if entrou:
         grafico.append(g)
 
   #versao = request.GET.get('versao')
   versao = '2.0'

   alteracoes_medidor = RelatorioAlteracoesMedidor.objects.all().filter(consumer=consumer).filter(justificado = True).filter(~Q(justificativa__contains = '!BATCH!'))
   corrente_zerada = RelatorioCorrenteZerada.objects.all().filter(consumer=consumer).filter(justificado = True).filter(~Q(justificativa__contains = '!BATCH!'))
   tensao_zerada = RelatorioTensaoZerada.objects.all().filter(consumer=consumer).filter(justificado = True).filter(~Q(justificativa__contains = '!BATCH!'))
   queda_consumo = RelatorioQuedaDeConsumo.objects.all().filter(consumer=consumer).filter(justificado = True).filter(~Q(justificativa__contains = '!BATCH!'))
   mm_versus_consumo = RelatorioMMVersusConsumo.objects.all().filter(consumer=consumer).filter(justificado = True).filter(~Q(justificativa__contains = '!BATCH!'))

   alarmes = []

   for i in alteracoes_medidor:
      alarme = Alarmes()
      alarme.referencia = i.data_alteracao.date
      alarme.justificativa = i.justificativa
      alarme.data_hora = i.data_hora
      alarme.tipo = "Alteracoes do medidor"
      alarme.analista = i.user
      alarme.alvo_gerado = i.alvo_gerado

      alarmes.append(alarme)

   for i in corrente_zerada:
      alarme = Alarmes()
      alarme.referencia = i.inicio.date()
      alarme.justificativa = i.justificativa
      alarme.data_hora = i.data_hora
      alarme.tipo = "Corrente Zerada"
      alarme.analista = i.user
      alarme.alvo_gerado = i.alvo_gerado

      alarmes.append(alarme)

   for i in tensao_zerada:
      alarme = Alarmes()
      alarme.referencia = i.inicio.date()
      alarme.justificativa = i.justificativa
      alarme.data_hora = i.data_hora
      alarme.tipo = "Tensao Zerada"
      alarme.analista = i.user
      alarme.alvo_gerado = i.alvo_gerado

      alarmes.append(alarme)

   for i in queda_consumo:
      alarme = Alarmes()
      alarme.referencia = i.referencia
      alarme.justificativa = i.justificativa
      alarme.data_hora = i.data_hora
      alarme.tipo = "Queda Consumo"
      alarme.analista = i.user
      alarme.alvo_gerado = i.alvo_gerado

      alarmes.append(alarme)

   for i in mm_versus_consumo:
      alarme = Alarmes()
      alarme.referencia = i.mes_referencia
      alarme.justificativa = i.justificativa
      alarme.data_hora = i.data_hora
      alarme.tipo = "MM Versus Consumo"
      alarme.analista = i.user
      alarme.alvo_gerado = i.alvo_gerado

      alarmes.append(alarme)

   #alarmes = sorted(alarmes,key = lambda x: x.referencia,reverse=True)
   
   mms = sorted(mms,key = lambda x: x.date_hour,reverse=True)

   context = { 'company_session': company_session, 'consumer' : consumer, 'inspections':inspections, 'grafico' : grafico, 'alarmes':alarmes, 'mms':mms,}

   if versao == "2.0":
      template = loader.get_template('consumer_detailv2.0.html')
   else:
      template = loader.get_template('consumer_detail_new.html')

   return HttpResponse(template.render(context,request))

@login_required(login_url='/admin/login/')
def my_404(request):
   context = { }
   template = loader.get_template('404.html')

   return HttpResponse(template.render(context,request))


@login_required(login_url='/admin/login/')
def mm(request,consumer_id):
   company_session = Company.objects.get(name=request.session['Company'])

   qt1 = request.GET.get('qt1')
   qt2 = request.GET.get('qt2')
   qt3 = request.GET.get('qt3')

   data_de = request.GET.get('data_de')
   data_ate = request.GET.get('data_ate')

   consumer = Consumer.objects.get(id=consumer_id)
   channel1_qty = Quantity.objects.get(quantity=qt1)
   channel2_qty = Quantity.objects.get(quantity=qt2)
   channel3_qty = Quantity.objects.get(quantity=qt3)

   if request.method == 'POST':
      form = FormMM(request.POST)
   else:
      form = FormMM()

   if form.is_valid():
      data_de = form.cleaned_data['data_de']
      data_ate = form.cleaned_data['data_ate']
   
      history = consumer.history_set.all().filter(date_hour__lte=form.cleaned_data['data_ate']+timedelta(hours=23,minutes=59,seconds=0)).filter(date_hour__gte=form.cleaned_data['data_de']).filter(channel_1_qty=channel1_qty).filter(channel_2_qty=channel2_qty).filter(channel_3_qty=channel3_qty).order_by('date_hour')
   else:
      if data_de and data_ate:
         data_de = datetime.strptime(data_de,"%d/%m/%Y %H:%M")
         data_ate = datetime.strptime(data_ate,"%d/%m/%Y %H:%M")

         history = consumer.history_set.all().filter(date_hour__lte=data_ate).filter(date_hour__gte=data_de).filter(channel_1_qty=channel1_qty).filter(channel_2_qty=channel2_qty).filter(channel_3_qty=channel3_qty).order_by('date_hour')         
      else:
         history = consumer.history_set.all().filter(channel_1_qty=channel1_qty).filter(channel_2_qty=channel2_qty).filter(channel_3_qty=channel3_qty).order_by('date_hour')

         paginator = Paginator(history,1440)
         page = request.GET.get('page')

         try:
            history = paginator.page(page)
         except PageNotAnInteger:
            history = paginator.page(1)
         except EmptyPage:
            history = paginator.page(paginator.num_pages)
   try:
      context = { 'company_session': company_session, 'consumer' : consumer, 'history' : history, 'form' : form, 'data_de':data_de.strftime("%d/%m/%Y %H:%I"), 'data_ate':data_ate.strftime("%d/%m/%Y %H:%I"),}
   except AttributeError:
      context = { 'company_session': company_session, 'consumer' : consumer, 'history' : history, 'form' : form,}

   template = loader.get_template('mm.html')

   return HttpResponse(template.render(context,request))


