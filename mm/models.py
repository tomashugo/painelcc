from __future__ import unicode_literals

from django.db import models
from crews.models import Region

# Create your models here.

class Quantity(models.Model):
   code = models.CharField(max_length=2)
   quantity = models.CharField(max_length=5)

   class Meta:
      verbose_name = "Grandeza"

   def __str__(self):
      return self.quantity



class Company(models.Model):
   name = models.CharField(max_length=20)
   class Meta:
      verbose_name = "Empresa"

   def __str__(self):
      return self.name


class Meter(models.Model):
   serial = models.CharField(max_length=11)
   company = models.ForeignKey(Company,blank=True,null=True)

   def __str__(self):
      return self.serial

   class Meta:
      verbose_name = "Medidor"
      verbose_name_plural = "Medidores"


class Consumer(models.Model):
   company = models.ForeignKey(Company, blank=True, null=True)
   installation = models.CharField(max_length=30, blank=True)
   name = models.CharField(max_length=100, blank=True)
   city = models.CharField(max_length=50, blank=True)
   region = models.ForeignKey(Region,default=6)
   revenue = models.CharField(max_length=1, blank=True)
   public_place = models.CharField(max_length=50,blank=True)
   reference = models.CharField(max_length=200,blank=True)
   complement = models.CharField(max_length=50,blank=True)

   class Meta:
      verbose_name = "Consumidor"
      verbose_name_plural = "Consumidores"

   def __str__(self):
      return self.installation.encode("utf-8") + " - ".encode("utf-8") + self.name.encode("utf-8")

class MeterHistory(models.Model):
   since = models.DateTimeField('valido desde')
   until = models.DateTimeField('valido ate')
   meter = models.ForeignKey(Meter,related_name='meterhistory')
   consumer = models.ForeignKey(Consumer)

   def __str__(self):
      return self.meter.serial


class Mm(models.Model):
   company = models.ForeignKey(Company,null=True,blank=True)
   archive = models.CharField(max_length=20)
   date_hour = models.DateTimeField('read hour')
   reader = models.CharField(max_length=6)
   serial = models.CharField(max_length=8)
   model = models.CharField(max_length=4)
   version = models.CharField(max_length=4)
   constant1 = models.CharField(max_length=13)
   constant2 = models.CharField(max_length=13)
   constant3 = models.CharField(max_length=13)
   channel_1_qty = models.ForeignKey(Quantity,related_name='channel1')
   channel_2_qty = models.ForeignKey(Quantity,related_name='channel2')
   channel_3_qty = models.ForeignKey(Quantity,related_name='channel3')
   last_integration = models.DateTimeField('ultima integracao')
   last_bill = models.DateTimeField('ultima fatura')
   penultimate_bill = models.DateTimeField('penultima fatura')
   meter_object = models.ForeignKey(Meter,blank=True,null=True)
   status_batery = models.CharField(max_length=2,blank=True,null=True)
   path = models.CharField(max_length=100,blank=True,null=True)

   #def __str__(self):
   #   return unicode(self.archive)

class EnergyFault(models.Model):
   begin_hour = models.DateTimeField('inicio da falta')
   end_hour   = models.DateTimeField('fim da falta')
   consumer = models.ForeignKey(Consumer)
   duration = models.FloatField(null=True,blank=True)

class History(models.Model):
   consumer = models.ForeignKey(Consumer)
   date_hour = models.DateTimeField('timestamp')
   channel_1_value = models.FloatField()
   channel_2_value = models.FloatField()
   channel_3_value = models.FloatField()
   channel_1_qty   = models.ForeignKey(Quantity,related_name='channel1_history')
   channel_2_qty   = models.ForeignKey(Quantity,related_name='channel2_history')
   channel_3_qty   = models.ForeignKey(Quantity,related_name='channel3_history')
   channel_1_pulse = models.IntegerField(blank=True)
   channel_2_pulse = models.IntegerField(blank=True)
   channel_3_pulse = models.IntegerField(blank=True)
   mm = models.ForeignKey(Mm,blank=True)

class Change(models.Model):
   code = models.CharField(max_length=2)
   observation = models.CharField(max_length=86,null=True,blank=True)
   meter = models.ForeignKey(Meter,blank=True,null=True)
   leitor = models.CharField(max_length=6,null=True,blank=True)
   date_time = models.DateTimeField('data da alteracao',null=True,blank=True)

class Holiday(models.Model):
   holiday = models.DateTimeField('feriado')
   mm = models.ForeignKey(Mm)

class Unprocessed(models.Model):
   archive = models.CharField(max_length=20)
   msg = models.TextField()
