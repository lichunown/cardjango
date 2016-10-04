from django.conf.urls import include, url
from django.contrib import admin
from . import views 


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^car', views.car,name='car'), 
    url(r'^getstatus', views.getstatus,name='getstatus'),    
    url(r'^changeport', views.changeport,name='changeport'),      
	]
