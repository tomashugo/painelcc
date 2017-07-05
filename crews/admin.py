from django.contrib import admin

# Register your models here.

from .models import Role, Employee, Region, Crew, DayOff, Car, CarHistory


class EmployeeAdmin (admin.ModelAdmin):
   list_display = ('registration','name','role')
   search_fields = ('name','registration')

class CrewAdmin (admin.ModelAdmin):
   list_display = ('technician','eletrician','region')
   search_fields = ['car__plate']   

class DayOffAdmin (admin.ModelAdmin):
   list_display = ('employee','day_off')
   list_filter = ['employee','day_off']

class CarHistoryInline(admin.StackedInline):
   model = CarHistory
   extra = 3

class CarAdmin (admin.ModelAdmin):
   def last_km_history(self):
      history = self.carhistory_set.all()

      if len(history) > 0:
         return history.last().km + " em " + history.last().date_km.strftime("%d/%m/%Y")
      else:
         return "NA"   

   def crew(self):
      crew = self.crew_set.all()
      
      if len(crew) >0:
         return crew.last()
      else:
         return "NA"

   list_display = ('plate','model',crew,'km_last_revision','revision',last_km_history)
   search_fields = ['plate']
   inlines = [CarHistoryInline]


admin.site.register(Role)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Region)
admin.site.register(Crew,CrewAdmin)
admin.site.register(DayOff,DayOffAdmin)
admin.site.register(Car,CarAdmin)
