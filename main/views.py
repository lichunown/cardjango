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
    option = request.GET.get("option")
    devileft = request.GET.get("DEVIleft",None)
    deviright = request.GET.get("DEVIright",None)
    leftspeed = request.GET.get("leftspeed",100)
    rightspeed = request.GET.get("rightspeed",100)    
    if option=="run":
        (l,r) = car.go(leftspeed,rightspeed,devileft,deviright)
    elif option=="leftgo":
        l = car.leftgo(leftspeed,devileft)
    elif option=="leftback":
        l = car.leftback(leftspeed,devileft)
    elif option=="rightgo":
        r = car.rightgo(rightspeed,deviright)
    elif option=="rightback":
        r = car.rightback(rightspeed,deviright)
    elif option=="stop":
        car.stop()
        l = 0
        r = 0
    elif option=="back":
        (l,r) = car.back()
    elif option=="leftstop":
        car.leftstop()
        l = 0
    elif option=="rightstop":
        car.rightstop()
        r = 0
    elif option=="shell":
        cmd = request.GET.get("cmd","")
        exec compile(cmd,'','exec')
        return HttpResponse(">>>"str(cmd))
    else:
        return HttpResponse("errorGET:"+str(request.GET)) 
    return HttpResponse("ok:"+"left:"+str(100-int(l))+"right:"+str(100-int(r))) 

