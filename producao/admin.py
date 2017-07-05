from django.contrib import admin

from .models import Producao, TipoServico, AlvosAbertos, AlvosDespachados

# Register your models here.
class ProducaoAdmin(admin.ModelAdmin):
   list_display = ['envio','tipo_servico','tecnico','instalacao','regional','codigo','familia_codigo','data_realizacao','observacao']
   search_fields = ['instalacao']

class AlvosAbertosAdmin(admin.ModelAdmin):
   list_display = ['ns','consumer','data_geracao','observacao']
   search_fields = ['consumer__installation','consumer__name']

class AlvosDespachadosAdmin(admin.ModelAdmin):
   list_display = ['ns','consumer','inspetor','data_despacho']
   
   def ns(self,obj):
      return obj.alvo_aberto.ns

   def consumer(self,obj):
      return unicode(obj.alvo_aberto.consumer.installation) + " - " + unicode(obj.alvo_aberto.consumer.name)


admin.site.register(AlvosAbertos,AlvosAbertosAdmin)
admin.site.register(Producao,ProducaoAdmin)
admin.site.register(TipoServico)
admin.site.register(AlvosDespachados,AlvosDespachadosAdmin)
