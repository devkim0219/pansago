"""pansago URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import law.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', law.views.index, name='index'),
    path('', law.views.index, name='index'),
    path('preclist/', law.views.preclist, name='preclist'),
    path('showChart/', law.views.showChart, name='showChart'),
    path('precDetail/', law.views.precDetail, name='precDetail'),
    path('showChart/', law.views.showChart, name='showChart'),
    path('showwc/', law.views.showwc, name='showwc'),
    path('dictionaryhome/', law.views.dictionaryhome, name='dictionaryhome'),
    path('chartSearch/', law.views.chartSearch, name='chartSearch'),
]