from __future__ import unicode_literals

from django.db import models
from crews.models import Employee, Region
from mm.models import Consumer

# Create your models here.

class TipoServico(models.Model):
   nome = models.CharField(max_length = 20,blank=True,null=True)

   def __unicode__(self):
      return self.nome

class Producao(models.Model):
   envio = models.DateTimeField('envio')
   tipo_servico = models.ForeignKey(TipoServico)
   tecnico = models.ForeignKey(Employee)
   instalacao = models.CharField(max_length = 20,blank=True,null=True)
   regional = models.ForeignKey(Region)
   codigo = models.CharField(max_length = 3,blank=True,null=True)
   familia_codigo = models.CharField(max_length = 3,blank=True,null=True)
   data_realizacao = models.DateField('data_realizacao')
   observacao = models.TextField(blank=True,null=True)
   data_devolucao = models.DateField('data_devolucao',blank=True,null=True)

class AlvosAbertos(models.Model):
   ns = models.CharField(max_length=12,blank=True,null=True)
   data_geracao = models.DateField('data_geracao')
   consumer = models.ForeignKey(Consumer)
   observacao = models.TextField(blank=True,null=True)

class AlvosDespachados(models.Model):
   alvo_aberto = models.ForeignKey(AlvosAbertos)
   data_despacho = models.DateField('data_despacho')
   inspetor = models.ForeignKey(Employee)
