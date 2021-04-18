from django.shortcuts import render
from app.models import *


# Create your views here.
def home(request):
    return render(request, "layout.html")


def infoProducer(request, id):
    try:
        producer = Producer.objects.get(id=id)
        return render(request, "infoProducer.html", {"producer": producer})
    except:
        producer = None
        return render(request, "infoProducer.html")

def infoActor(request,id):
    try:
        actor = Actor.objects.get(id=id)
        return render(request,"infoActor.html",{"actor":actor})
    except:
        producer = None
        return render(request,"infoActor.html")
