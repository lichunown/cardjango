from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from gpio import port,run
# Create your views here.

# try:
#     port.init()
# except Exception,e:
#     print e

car = run.Car()

@csrf_exempt
def index(request):
    # content={
    #     'ports':[7,11,12,13,15,16,18,22,29,30,31,32,33,35,36,37,38,40],
    #     'maxport':40,
    # }
    # return render(request,"index.html",content)
    pass


@csrf_exempt
def getstatus(request):
    return HttpResponse(json.dumps(port.getstatus()))

@csrf_exempt
def changeport(request):
    if request.method=="POST":
        if request.POST.get("port",""):
            result = port.changestat(int(request.POST.get("port","")))
            return HttpResponse(result)  

@csrf_exempt
def runcar(request):
    option = request.GET.get("option")
    if option=="run":
        car.go()
    elif option=="leftgo":
        car.leftgo()
    elif option=="leftback":
        car.leftback()
    elif option=="rightgo":
        car.rightgo()
    elif option=="rightback":
        car.rightback()
    elif option=="stop":
        car.stop()
    elif option=="stopleft":
        car.stopleft()
    elif option=="stopright":
        car.stopright()
    else:
        return HttpResponse("error") 
    return HttpResponse("ok") 


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