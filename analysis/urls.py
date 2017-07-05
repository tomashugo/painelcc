"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),

    url(r'^corrente_zerada/$',views.corrente_zerada,name='corrente_zerada'),
    url(r'^corrente_zerada/(?P<consumer_id>[0-9]+)/recorrencia$',views.recorrencia_corrente_zerada,name='recorrencia_corrente_zerada'),
    url(r'^form_corrente_zerada/$',views.form_corrente_zerada,name='form_corrente_zerada'),

    url(r'^tensao_zerada/$',views.tensao_zerada,name='tensao_zerada'),
    url(r'^tensao_zerada/(?P<consumer_id>[0-9]+)/recorrencia$',views.recorrencia_tensao_zerada,name='recorrencia_tensao_zerada'),
    url(r'^form_tensao_zerada/$',views.form_tensao_zerada,name='form_tensao_zerada'),

    url(r'^mm_versus_consumo/$',views.mm_versus_consumo,name='mm_versus_consumo'),
    url(r'^form_mm_versus_consumo/$',views.form_mm_versus_consumo,name='form_mm_versus_consumo'),
    url(r'^download/$',views.download,name='download'),
    url(r'^alteracoes_medidor/$',views.alteracoes_medidor,name='alteracoes_medidor'),

    url(r'^fraude_nao_incrementada/$',views.fraude_nao_incrementada,name='fraude_nao_incrementada'),
    url(r'^form_fraude_nao_incrementada/$',views.form_fraude_nao_incrementada,name='form_fraude_nao_incrementada'),

    url(r'^queda_consumo/$',views.queda_consumo,name='queda_consumo'),
    url(r'^producao/$',views.producao,name='producao'),

    url(r'^form_queda_consumo/$',views.form_queda_consumo,name='form_queda_consumo'),

    url(r'^form_alteracoes_medidor/$',views.form_alteracoes_medidor,name='form_alteracoes_medidor'),
    url(r'^tc_saturado/$',views.tc_saturado,name='tc_saturado'),
    url(r'^download_mm/$',views.download_mm,name='download_mm'),

    url(r'^produtividade/$',views.produtividade,name='produtividade'),

    url(r'^ver_produtividade/(?P<analista>[a-z]+)/(?P<diames>[0-9]+)$',views.ver_produtividade,name='ver_produtividade'),
]
