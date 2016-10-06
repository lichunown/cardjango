from django.conf.urls import include, url
from django.contrib import admin
from . import views 


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^car', views.runcar,name='car'), 
    # url(r'^go', views.go,name='go'), 
    # url(r'^leftgo', views.leftgo,name='leftgo'),
    # url(r'^leftback', views.leftback,name='leftback'),
    # url(r'^rightgo', views.rightgo,name='rightgo'), 
    # url(r'^rightback', views.rightback,name='rightback'), 
    # url(r'^stop', views.stop,name='stop'), 
    # url(r'^stopleft', views.stopleft,name='stopleft'),
    # url(r'^stopright', views.stopright,name='stopright'),
    url(r'^getstatus', views.getstatus,name='getstatus'),    
    url(r'^changeport', views.changeport,name='changeport'),      
	]
