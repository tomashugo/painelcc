from django import forms
from adm.models import Sheet

class UploadFileForm(forms.ModelForm):
   class Meta:
      model = Sheet
      fields = ['company','type']

   file = forms.FileField()
