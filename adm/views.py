from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from openpyxl import Workbook, load_workbook
import os, random
from adm.models import Sheet
import datetime
from django.contrib.auth.decorators import login_required
from mm.models import Company


# Create your views here.
@login_required(login_url='/admin/login/')
def index(request):
   company_session = Company.objects.get(name=request.session['Company'])
   
   if request.method == 'POST':
      form = UploadFileForm(request.POST,request.FILES)
      if form.is_valid():              
         file = request.FILES['file']

         try:
            wb = load_workbook(filename=file)
         except Exception:
            return HttpResponse("ERRO: O arquivo deve estar em formato \"Pasta de Trabalho do Excel (*.xlsx)\"")

         path = "/home/tomash/painelcc/planilhas/" + file.name

         post = form.save(commit=False)
         post.path = path
         post.processed = False
         post.date_time_processed = datetime.datetime.now()
	 post.save()

         ws = wb.active

         xlsx = os.path.join("/home/tomash/painelcc/planilhas",file.name)
         wb.save(xlsx)

   	 return HttpResponse("Deu certo")
   else:
      form = UploadFileForm()

   return render(request,'adm/uploadv2.0.html',{'form':form,'company_session':company_session,})
