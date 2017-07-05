from openpyxl import load_workbook
from django.core.wsgi import get_wsgi_application

import os
import sys

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE","painelcc.settings")
   application = get_wsgi_application()

   from django.db import models
   from crews.models import Region
   from mm.models import Consumer, Meter, MeterHistory, Company
   from analysis.models import Billing, Register
   from datetime import datetime
   from django.shortcuts import get_object_or_404
   from adm.models import Type, Sheet

   consumo = Type.objects.get(type="Consumo")
   planilhas = Sheet.objects.all().filter(type=consumo).filter(processed=False)

   for p in planilhas:
      company = p.company

      p.processed = True

      wb = load_workbook(filename=p.path)
      ws = wb['Exportar Planilha']

      codes = dict()

      codes['ZRCANP'] = Register.objects.get(code='EAP')
      codes['ZRCAFP'] = Register.objects.get(code='EAFP')
      codes['ZRCAT']  = Register.objects.get(code='EAT')
      codes['CON']    = Register.objects.get(code='EAT')
      codes['ZRCARV'] = Register.objects.get(code='EAR')
      codes['CRU']    = Register.objects.get(code='EAR')
      codes['CRT']    = Register.objects.get(code='EAR')
      codes['CRS']    = Register.objects.get(code='EAR')
      codes['CFU']    = Register.objects.get(code='EAFP')
      codes['CDF']    = Register.objects.get(code='EAFP')
      codes['CFP']    = Register.objects.get(code='EAFP')
      codes['CPU']    = Register.objects.get(code='EAP')
      codes['COP']    = Register.objects.get(code='EAP')
      codes['ETI']    = Register.objects.get(code='EAP')
      codes['CTP']    = Register.objects.get(code='EAP')
      codes['CDP']    = Register.objects.get(code='EAP')
      codes['CNP']    = Register.objects.get(code='EAP')
      codes['CNF']    = Register.objects.get(code='EAFP')

      for i in ws:
         if str(i[0].value) != 'COD_UN_CONS_HCO':
            installation = str(int(i[0].value))
            #print installation
            dta_ref_hco = datetime.strptime(i[1].value,"%d/%m/%y")
            qtd_dia_fat_hco = str(int(i[2].value))
            cod_mens_leit_hco = str(i[3].value)
            cod_tipo_espe_hco = str(i[4].value)
            qtd_cons_fat_hco = str(i[5].value)
            qtd_cons_corg_hco = str(i[6].value)


            dta_leit_inic = datetime.strptime(str(i[7].value),"%d/%m/%y")
            dta_leit_fim = datetime.strptime(str(i[8].value),"%d/%m/%y")
         
            try:
               #consumer = get_object_or_404(Consumer,installation=installation)
               consumer = Consumer.objects.get(installation=installation,company=company)
            except Consumer.DoesNotExist:
               continue

            billing = Billing.objects.all().filter(consumer=consumer).filter(reference=dta_ref_hco).filter(code_type=codes[cod_tipo_espe_hco]).filter(billed=qtd_cons_fat_hco)

            if len(billing) == 0:
               adicionar = Billing()
               adicionar.consumer = consumer
               adicionar.reference = dta_ref_hco
               adicionar.revenue_days = int(qtd_dia_fat_hco)
               adicionar.reader_msg = cod_mens_leit_hco
               adicionar.code_type=codes[cod_tipo_espe_hco]
               adicionar.read=qtd_cons_corg_hco
               adicionar.billed=qtd_cons_fat_hco
               adicionar.init_cycle=dta_leit_inic 
               adicionar.end_cycle=dta_leit_fim
               adicionar.save()

               
      p.save()
