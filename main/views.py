from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from gpio import port,run
# Create your views here.

port.init()
car = run.Car()

@csrf_exempt
def index(request):
    content={
        'ports':[7,11,12,13,15,16,18,22,29,30,31,32,33,35,36,37,38,40],
        'maxport':40,
    }
    return render(request,"index.html",content)


@csrf_exempt
def getstatus(request):
    return HttpResponse(json.dumps(port.getstatus()))

@csrf_exempt
def changeport(request):
    if request.method=="POST":
        if request.POST.get("port",""):
            result = port.changestat(int(request.POST.get("port","")))
            return HttpResponse(result)    

def car(request):
    pass

@csrf_exempt
def go(request):
    car.run()
    return HttpResponse("ok") 
@csrf_exempt
def leftgo(request):
    car.leftgo()
    return HttpResponse("ok") 
@csrf_exempt
def leftback(request):
    car.leftback()
    return HttpResponse("ok")     
@csrf_exempt
def rightgo(request):
    car.rightgo()
    return HttpResponse("ok") 
@csrf_exempt
def rightback(request):
    car.rightback()
    return HttpResponse("ok")     
@csrf_exempt
def stop(request):
    car.stop()
    return HttpResponse("ok")      
@csrf_exempt
def stopleft(request):
    car.stopleft()
    return HttpResponse("ok")   
@csrf_exempt
def stopright(request):
    car.stopright()
    return HttpResponse("ok")   