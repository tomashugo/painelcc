from django.contrib import admin

# Register your models here.

from .models import Inspection, Billing, Register, AlarmType, Alarm, RelatorioAlteracoesMedidor, RelatorioCorrenteZerada, RelatorioTensaoZerada, RelatorioMMVersusConsumo, RelatorioQuedaDeConsumo, Protocolo, Directory, RelatorioFraudeNaoIncrementada

class ProtocoloAdmin(admin.ModelAdmin):
   list_display = ('equipe','consumidor','data')
#   list_filter = ('data')

class InspectionAdmin (admin.ModelAdmin):
   list_display = ('ns','consumer','date_time_executed')
   search_fields = ['consumer__name','consumer__installation','ns']

class BillingAdmin (admin.ModelAdmin):
   list_display = ('consumer','reference','revenue_days','reader_msg','code_type','read','billed','init_cycle','end_cycle')
   search_fields = ['consumer__name','consumer__installation']

class RelatorioAlteracoesMedidorAdmin (admin.ModelAdmin):
   list_display = ('consumer','data_alteracao','leitor','code','observacao','justificado','user','justificativa','expira','data_hora')
   list_filter = ('data_hora','user')

class RelatorioCorrenteZeradaAdmin (admin.ModelAdmin):
   list_display = ('company','consumer','inicio','fim','ia','ib','ic','justificado','user','justificativa','data_hora')
   search_fields = ['consumer__installation','consumer__name','justificativa']
   list_filter = ('data_hora','user','company')

class RelatorioTensaoZeradaAdmin (admin.ModelAdmin):
   list_display = ('consumer','company','inicio','fim','va','vb','vc','justificado','user','justificativa','data_hora')
   search_fields = ['consumer__installation','consumer__name','justificativa']
   list_filter = ('data_hora','user','company')

class RelatorioMMVersusConsumoAdmin (admin.ModelAdmin):
   list_display = ('consumer','meter','mes_referencia','consumo_faturado','consumo_mm','tipo_comparacao','mm','justificado')
   search_fields = ['consumer__installation','consumer__name','justificativa']
   list_filter = ('data_hora','user')

class RelatorioQuedaDeConsumoAdmin (admin.ModelAdmin):
   list_display = ('consumer','referencia','media_consumo','consumo_referencia','justificado')
   search_fields = ['consumer__installation','consumer__name','justificativa']
   list_filter = ('justificado','user','company')

class DirectoryAdmin (admin.ModelAdmin):
   list_display = ('company','directory','data_hora')

class RelatorioFraudeNaoIncrementadaAdmin(admin.ModelAdmin):
   list_display = ('company','consumer','mes_fraude','code_fraude','faturamento_anterior','faturamento_posterior')
   list_filter = ['company','code_fraude','justificado']
   search_fields = ['consumer__installation','consumer__name','justificativa']

admin.site.register(RelatorioFraudeNaoIncrementada,RelatorioFraudeNaoIncrementadaAdmin)
admin.site.register(Inspection,InspectionAdmin)
admin.site.register(Register)
admin.site.register(Billing,BillingAdmin)
admin.site.register(AlarmType)
admin.site.register(Alarm)
admin.site.register(RelatorioAlteracoesMedidor,RelatorioAlteracoesMedidorAdmin)
admin.site.register(RelatorioCorrenteZerada,RelatorioCorrenteZeradaAdmin)
admin.site.register(RelatorioTensaoZerada,RelatorioTensaoZeradaAdmin)
admin.site.register(RelatorioMMVersusConsumo,RelatorioMMVersusConsumoAdmin)
admin.site.register(RelatorioQuedaDeConsumo,RelatorioQuedaDeConsumoAdmin)
admin.site.register(Protocolo,ProtocoloAdmin)
admin.site.register(Directory,DirectoryAdmin)
