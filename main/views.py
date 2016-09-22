from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from gpio import port
# Create your views here.

port.init()


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