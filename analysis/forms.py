from django import forms
from django.forms import ModelForm
from .models import RelatorioMMVersusConsumo
from producao.models import Producao

class FormBillingMM(forms.Form):
   referencia = forms.DateField(label='Referencia')

class TheForm(ModelForm):
   class Meta:
      model = RelatorioMMVersusConsumo
      fields = ['justificativa']

class UploadFileForm(forms.ModelForm):
   file = forms.FileField()

