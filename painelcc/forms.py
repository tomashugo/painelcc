from django import forms

from django.conf import settings
from django.contrib.admin import widgets


class FormMM(forms.Form):
   data_de = forms.DateTimeField(label='Desde',input_formats=['%d/%m/%Y','%d/%m/%y','%d/%m/%Y %H:%I'])
   data_ate = forms.DateTimeField(label='Ate',input_formats=['%d/%m/%Y','%d/%m/%y','%d/%m/%Y %H:%I'])
