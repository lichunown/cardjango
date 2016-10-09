from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from gpio import run,port
# Create your views here.

try:
    port.init()
except Exception,e:
    print e

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
r = 0
l = 0
@csrf_exempt
def runcar(request):
    global r,l
    option = request.GET.get("option")
    devileft = request.GET.get("DEVIleft",None)
    deviright = request.GET.get("DEVIright",None)    
    if option=="run":
        (l,r) = car.go(devileft,deviright)
    elif option=="leftgo":
        l = car.leftgo(devileft)
    elif option=="leftback":
        l = car.leftback(devileft)
    elif option=="rightgo":
        r = car.rightgo(deviright)
    elif option=="rightback":
        r = car.rightback(deviright)
    elif option=="stop":
        car.stop()
    elif option=="leftstop":
        car.leftstop()
    elif option=="rightstop":
        car.rightstop()
    else:
        return HttpResponse("error\nGET:"+str(request.GET)) 
    return HttpResponse("ok:"+"left"+str(l)+"right"+str(r)) 


# @csrf_exempt
# def go(request):
#     global car
#     car.run()
#     return HttpResponse("ok") 
# @csrf_exempt
# def leftgo(request):
#     global car    
#     car.leftgo()
#     return HttpResponse("ok") 
# @csrf_exempt
# def leftback(request):
#     global car    
#     car.leftback()
#     return HttpResponse("ok")     
# @csrf_exempt
# def rightgo(request):
#     global car    
#     car.rightgo()
#     return HttpResponse("ok") 
# @csrf_exempt
# def rightback(request):
#     global car    
#     car.rightback()
#     return HttpResponse("ok")     
# @csrf_exempt
# def stop(request):
#     global car    
#     car.stop()
#     return HttpResponse("ok")      
# @csrf_exempt
# def stopleft(request):
#     global car    
#     car.stopleft()
#     return HttpResponse("ok")   
# @csrf_exempt
# def stopright(request):
#     global car    
#     car.stopright()
#     return HttpResponse("ok")   