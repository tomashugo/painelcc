from django.contrib import admin
from adm.models import Type, Sheet

# Register your models here.

class TypeAdmin(admin.ModelAdmin):
   list_display = ['type']

class SheetAdmin(admin.ModelAdmin):
   list_display = ['company','type','path','processed','date_time_processed']

admin.site.register(Type,TypeAdmin)
admin.site.register(Sheet,SheetAdmin)
