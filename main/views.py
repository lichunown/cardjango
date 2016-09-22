from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from gpio import port
# Create your views here.

port.init()

@csrf_exempt
def index(request):
    content={
        'ports':[1,2,3,4,5],
        'maxport':25,
    }
    if request.method=="POST":
        if request.POST.get("port",""):
            result = port.sethigh(int(request.POST.get("port","")))
            return HttpResponse(result)
    else:
        return render(request,"index.html",content)