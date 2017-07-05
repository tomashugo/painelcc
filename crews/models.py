from django.db import models

class Region(models.Model):
   name = models.CharField (max_length=20) 

   class Meta:
      verbose_name = "Regional"
      verbose_name_plural = "Regionais"

   def __str__(self):
      return self.name

class Role(models.Model):
   role_name = models.CharField (max_length=100)
   seniority = models.CharField (max_length=2)

   class Meta:
      verbose_name = "Cargo"

   def __str__(self):
       return self.role_name + " " + self.seniority

class Employee(models.Model):
   registration = models.CharField(max_length=6,default="u0000")
   name = models.CharField (max_length=100)
   role = models.ForeignKey(Role)

   class Meta:
      ordering = ('name',)
      verbose_name = "Colaborador"
      verbose_name_plural = "Colaboradores"

   def __str__(self):
      return self.name.encode('utf8')

   def __unicode___(self):
      return self.name.encode('utf8')

class Car(models.Model):
   model = models.CharField(max_length=20)
   plate = models.CharField(max_length=8)
   revision = models.DateTimeField('ultima revisao')
   km_last_revision = models.CharField(max_length=10,default="0")
 
   class Meta:
      verbose_name = "Viatura"

   def __str__(self):
      return self.plate

class CarHistory(models.Model):
   car = models.ForeignKey(Car)
   date_km = models.DateTimeField('data do km')
   km = models.CharField(max_length=6)

   def __str__(self):
      return self.km

class Crew(models.Model):
   technician = models.ForeignKey(Employee,related_name="technician")
   eletrician = models.ForeignKey(Employee,related_name="eletrician")
   region = models.ForeignKey(Region)
   car = models.ForeignKey(Car)
  
   class Meta:
      verbose_name = "Equipe"


   def __str__(self):
      return self.technician.__str__() + " & " + self.eletrician.__str__()

class DayOff(models.Model):
   employee = models.ForeignKey(Employee)
   day_off = models.DateTimeField('dia de folga')
  
   class Meta:
      verbose_name = "Folga"
