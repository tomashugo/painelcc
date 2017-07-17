from django.contrib import admin

import datetime

# Register your models here.

from .models import Consumer, Meter, MeterHistory, Quantity, Mm, Holiday, History, Change, Company, Unprocessed
from analysis.models import Inspection

class MmInline(admin.StackedInline):
    model = Mm
    extra = 0 

class MeterHistoryInline(admin.StackedInline):
    model = MeterHistory
    extra = 0

class InspectionInline(admin.StackedInline):
    model = Inspection
    extra = 0

class ConsumerAdmin(admin.ModelAdmin):
    def ultima_inspecao(self):
       ultima_inspecao = self.inspection_set.all().order_by('date_time_executed')

       if len(ultima_inspecao) > 0:
          return ultima_inspecao.last().date_time_executed.strftime("%d/%m/%Y")
       else:
          return "NA"

    def meter(self):
       meter = MeterHistory.objects.filter(until__gte =  datetime.date.today()).filter(consumer = self)

       if len(meter) > 0:
          return meter.first()

    list_display = ('company','installation','name',meter,'city','public_place','reference','complement','region','revenue',ultima_inspecao)
    list_filter = ['region','revenue','company']
    search_fields = ['installation','name']
    inlines = [MeterHistoryInline,InspectionInline]

class MeterAdmin(admin.ModelAdmin):
    search_fields = ['serial']
    list_display = ['serial','company']
    list_filter = ['company']
    inlines = [MeterHistoryInline,MmInline]

class MmAdmin(admin.ModelAdmin):
    search_fields = ['archive','serial']
    list_display = ('archive','company','date_hour','reader','serial','channel_1_qty','channel_2_qty','channel_3_qty')
    list_filter = ['company']

class HolidayAdmin(admin.ModelAdmin):
    search_fields = ['holiday','mm__archive']
    list_display = ['holiday','mm']

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['consumer','mm','date_hour','channel_1_value','channel_2_value','channel_3_value','channel_1_qty','channel_2_qty','channel_3_qty']
    search_fields = ['mm__archive','mm__serial','consumer__installation','consumer__name']
    ordering = ['date_hour']

class ChangeAdmin(admin.ModelAdmin):
    list_display= ['code','observation','meter','leitor','date_time']
    search_fields = ['code','observation']

class UnprocessedAdmin(admin.ModelAdmin):
    list_display = ['archive','msg']
    search_fields = ['archive','msg']

class MeterHistoryAdmin(admin.ModelAdmin):
    list_display = ['since','until','meter','consumer']
    search_fields = ['meter__serial','consumer__installation']

admin.site.register(MeterHistory,MeterHistoryAdmin)
admin.site.register(Unprocessed,UnprocessedAdmin)
admin.site.register(Company)
admin.site.register(Consumer,ConsumerAdmin)
admin.site.register(Meter,MeterAdmin)
admin.site.register(Quantity)
admin.site.register(Mm,MmAdmin)
admin.site.register(Holiday,HolidayAdmin)
#admin.site.register(History,HistoryAdmin)
admin.site.register(Change,ChangeAdmin)
