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
    url(r'^alvos_abertos/$',views.alvos_abertos,name='alvos_abertos'),
    url(r'^form_alvos_abertos/$',views.form_alvos_abertos,name='form_alvos_abertos'),
    url(r'^form_receber_alvo/$',views.form_receber_alvo,name='form_receber_alvo'),
    url(r'^alvos_despachados/$',views.alvos_despachados,name='alvos_despchados'),
    url(r'^alvos_nao_baixados/$',views.alvos_nao_baixados,name='alvos_nao_baixados'),
    url(r'^stats/$',views.stats,name='stats'),

]
