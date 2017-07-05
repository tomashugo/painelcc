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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.i18n import javascript_catalog

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^adm/',include('adm.urls')),
    url(r'^$',views.index,name='index'),
    #url(r'^consumer/$',include('mm.urls')),
    url(r'^consumer/$',views.consumer,name='consumer'),
    url(r'^consumer/(?P<consumer_id>[0-9]+)/detail$',views.consumer_detail,name='consumer_detail'),
    url(r'^consumer/(?P<consumer_id>[0-9]+)/mm/$',views.mm,name='mm'),    
    url(r'^analysis/',include('analysis.urls')),
    url(r'^producao/',include('producao.urls')),
    url(r'^admin/jsi18n', javascript_catalog,name='javascript_catalog'),
]

handler404 = "painelcc.views.my_404"
