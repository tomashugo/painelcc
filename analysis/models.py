from __future__ import unicode_literals

from django.db import models

from mm.models import Consumer, Meter, Mm, Company

from crews.models import Crew

# Create your models here.

class Register(models.Model):
    label = models.CharField(max_length=24)
    code = models.CharField(max_length=4)
    unity = models.CharField(max_length=5)

    class Meta:
       verbose_name = "Registrador"
       verbose_name_plural = "Registradores"

    def __str__(self):
       return self.label

class Estatisticas(models.Model):
    alvos_gerados = models.IntegerField()
    alvos_assertivos = models.IntegerField()
    alvos_justificados = models.IntegerField()
    alvos_nao_justificados = models.IntegerField()
    mm_anexadas = models.IntegerField()

class Billing(models.Model):
    consumer = models.ForeignKey(Consumer)
    reference = models.DateField('referencia')
    revenue_days = models.IntegerField()
    reader_msg = models.CharField(max_length=8,blank=True,null=True)
    code_type = models.ForeignKey(Register)
    read = models.FloatField()
    billed = models.FloatField()
    init_cycle = models.DateField('init_cycle')
    end_cycle  = models.DateField('end_cycle')

class Inspection(models.Model):
    consumer = models.ForeignKey(Consumer)
    ns = models.CharField(max_length=15,blank=True)
    code = models.CharField(max_length=3,blank=True)
    date_time_executed = models.DateTimeField('data da execucao')
    date_time_competence = models.DateTimeField('competencia da baixa',blank=True)
    date_time_load = models.DateTimeField('data da baixa')
    observation = models.TextField()

    class Meta:
        verbose_name = "Inspecao"
        verbose_name_plural = "Inspecoes"

    def __str__(self):
        return self.ns

class AlarmType(models.Model):
    label = models.CharField(max_length=40)

    def __str__(self):
       return self.label

class Alarm(models.Model):
    alarm_type = models.ForeignKey(AlarmType)
    consumer = models.ForeignKey(Consumer)
    date_hour_begin = models.DateTimeField('date_hour_begin')
    date_hour_end = models.DateTimeField('date_hour_end')
    value1 = models.FloatField()
    value2 = models.FloatField()
    value3 = models.FloatField()
    analyzed = models.BooleanField()
    reference = models.DateField('alarm_reference', null=True, blank=True)

class RelatorioQuedaDeConsumo(models.Model):
    company = models.ForeignKey(Company,blank=True,default=True)
    consumer = models.ForeignKey(Consumer)
    referencia = models.DateField('referencia')
    media_consumo = models.FloatField()
    consumo_referencia = models.FloatField()
    justificado = models.BooleanField(blank=True,default=False)
    # informacoes a respeito da resposta ao evento
    user = models.CharField(max_length=20,blank=True,null=True)
    justificativa = models.TextField(blank=True,null=True)
    data_expira = models.DateField('data_expira',blank=True,null=True)
    data_hora = models.DateTimeField('date_hour_justified',blank=True,null=True)
    alvo_gerado = models.BooleanField(blank=True,default=False)

class RelatorioAlteracoesMedidor(models.Model):
    company = models.ForeignKey(Company,blank=True,default=True)
    consumer = models.ForeignKey(Consumer)
    data_alteracao = models.DateTimeField('data_alteracao')
    leitor = models.CharField(max_length=6)
    code = models.CharField(max_length=2)
    observacao = models.CharField(max_length=86)
    justificado = models.BooleanField()
    # informacoes a respeito da resposta ao evento
    user = models.CharField(max_length=20,blank=True,null=True)
    justificativa = models.TextField(blank=True,null=True)
    expira = models.BooleanField(blank=True)
    data_hora = models.DateTimeField('date_hour_justified',blank=True,null=True)
    alvo_gerado = models.BooleanField(blank=True,default=False)

class RelatorioCorrenteZerada(models.Model):
    company = models.ForeignKey(Company,blank=True,null=True)
    consumer = models.ForeignKey(Consumer)
    inicio   = models.DateTimeField('inicio corrente zerada')
    fim      = models.DateTimeField('fim corrente zerada')
    ia       = models.FloatField()
    ib	     = models.FloatField()
    ic       = models.FloatField()
    justificado = models.BooleanField()
    # informacoes a respeito da resposta ao evento
    user = models.CharField(max_length=20,blank=True,null=True)
    justificativa = models.TextField(blank=True,null=True)
    data_expira = models.DateTimeField('data_expira',blank=True,null=True)
    data_hora = models.DateTimeField('date_hour_justified',blank=True,null=True)
    alvo_gerado = models.BooleanField(blank=True,default=False)

class RelatorioTensaoZerada(models.Model):
    company = models.ForeignKey(Company,blank=True,null=True)
    consumer = models.ForeignKey(Consumer)
    inicio   = models.DateTimeField('inicio tensao zerada')
    fim      = models.DateTimeField('fim tensao zerada')
    va       = models.FloatField()
    vb	     = models.FloatField()
    vc       = models.FloatField()
    justificado = models.BooleanField()
    # informacoes a respeito da resposta ao evento
    user = models.CharField(max_length=20,blank=True,null=True)
    justificativa = models.TextField(blank=True,null=True)
    data_expira = models.DateTimeField('data_expira',blank=True,null=True)
    data_hora = models.DateTimeField('date_hour_justified',blank=True,null=True)
    alvo_gerado = models.BooleanField(blank=True,default=False)

class RelatorioFraudeNaoIncrementada(models.Model):
    company = models.ForeignKey(Company,blank=True,null=True)
    consumer = models.ForeignKey(Consumer)
    mes_fraude = models.DateTimeField('mes_fraude')
    code_fraude = models.CharField(max_length=4)
    faturamento_anterior = models.FloatField()
    faturamento_posterior = models.FloatField()

    # informacoes a respeito da analise realizada
    justificado = models.BooleanField(blank=True)
    user = models.CharField(max_length=20,blank=True,null=True)
    justificativa = models.TextField(blank=True,null=True)
    data_expira = models.DateTimeField('data_expira',blank=True,null=True)
    data_hora = models.DateTimeField('date_hour_justified',blank=True,null=True)
    alvo_gerado = models.BooleanField(blank=True,default=False)

class RelatorioMMVersusConsumo(models.Model):
    company = models.ForeignKey(Company,blank=True,null=True)
    consumer = models.ForeignKey(Consumer)
    meter = models.ForeignKey(Meter)
    consumo_faturado = models.FloatField()
    consumo_mm = models.FloatField()
    tipo_comparacao = models.CharField(max_length=4)
    justificado = models.BooleanField()
    mes_referencia = models.DateField('mes_referencia')
    mm = models.ForeignKey(Mm,null=True,blank=True)

    user = models.CharField(max_length=20,blank=True,null=True)
    justificativa = models.TextField(blank=True,null=True)
    data_hora = models.DateTimeField('date_hour_justified',blank=True,null=True)
    alvo_gerado = models.BooleanField(blank=True,default=False)

class Protocolo(models.Model):
    equipe = models.ForeignKey(Crew)
    consumidor = models.ForeignKey(Consumer)
    data = models.DateTimeField()

    def __str__(self):
       return str(self.equipe) + " em " + str(self.consumidor) + " quando " + str(self.data)

class Directory(models.Model):
   company = models.ForeignKey(Company)
   directory = models.CharField(max_length=200)
   data_hora = models.DateTimeField()
