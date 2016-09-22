from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from gpio import port
# Create your views here.

port.init()


@csrf_exempt
def index(request):
    content={
        'ports':[7,11,12,13,15,16,18,22,29,30,31,32,33,35,36,37,38,40],
        'maxport':40,
        'highport':[],
    }
    if request.method=="POST":
        if request.POST.get("port",""):
            result = port.changestat(int(request.POST.get("port","")))
            content['highport']=port.getstatus()
            return HttpResponse(result)
    else:
        content['highport'] = port.getstatus()
        return render(request,"index.html",content)