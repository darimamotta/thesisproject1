"""thesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from . import views

from django.contrib import admin
from django.urls import path, include
from map import views as map_views
#from .finished_apps import simpleexample

urlpatterns = [
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
       #path('', cache_page(60)(views.index), name='dashboard-index'),
    path('admin/', admin.site.urls),
    path('', views.index, name='thesis-index'),
    path('page21.html', views.page21, name='thesis-page21'),
    path('sfh2.html', views.sfh2, name='thesis-sfh2'),
    path('mfh2.html', views.mfh2, name='thesis-mfh2'),
    path('commercial.html', views.commercial, name='thesis-commercial'),
    path('tos.html', views.tos, name='tos'),
    path('photo.html', views.photo, name='photo'),
    path('comb.html', views.comb, name='comb'),
    path('gas.html', views.gas, name='gas'),
    path('electric.html', views.electric, name='electric'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('pump.html', views.pump, name='pump'),
    path('hydro.html', views.hydro, name='hydro'),
    path('battery.html', views.battery, name='battery'),
    path('page1.html', views.page1, name='thesis-page1'),
    path('page2.html', views.page2, name='thesis-page2'),
    path('page3.html', views.page3, name='thesis-page3'),
    path('map.html', map_views.map, name='map'),
    #path('test_plotly.html', views.test, name='test'),
    #path('test_plotly.html', map_views.main1, name='test_plotly'),
    #path('test_plotly.html', map_views.index, name='test_plotly1'),
    #path('test_plotly.html', views.index1, name='test_plotly12'),
    #path('', views.home, name="home"),
    #path('', views.base, name="base")

]
