from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.
@csrf_exempt
def index(request):
    content={
        'ports':[1,2,3,4,5],
        'maxport':25,
    }
    if request.method=="POST":
        return HttpResponse(request.POST.get("port","none"))
    else:
        return render(request,"index.html",content)