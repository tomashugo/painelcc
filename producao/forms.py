from django import forms
from .models import Producao, AlvosAbertos, AlvosDespachados
from django.conf import settings
from django.contrib.admin import widgets

class ProducaoForm(forms.ModelForm):
   data_realizacao = forms.DateField(input_formats=['%d/%m/%Y'])
   class Meta:
      model = Producao
      data_realizacao = forms.DateField(widget=widgets.AdminDateWidget())
      fields = ['tipo_servico','tecnico','instalacao','regional','codigo','data_realizacao','familia_codigo','observacao']

class AlvosAbertosForm(forms.ModelForm):
   data_despacho = forms.DateField(input_formats=['%d/%m/%Y'])

   class Meta:
      model = AlvosDespachados
      fields = ['inspetor','data_despacho']

class ReceberAlvoForm(forms.ModelForm):
   data_devolucao = forms.DateField(input_formats=['%d/%m/%Y'])
   class Meta:
      model = Producao
      fields = ['data_devolucao']
