from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from gpio import port
# Create your views here.

port.init()

@csrf_exempt
def index(request):
    content={
        'ports':[x for x in range(1,27)],
        'maxport':26,
    }
    if request.method=="POST":
        if request.POST.get("port",""):
            result = port.changestat(int(request.POST.get("port","")))
            return HttpResponse(result)
    else:
        return render(request,"index.html",content)