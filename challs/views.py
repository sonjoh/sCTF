from django.shortcuts import render
from django.http import HttpResponse

#from sCTF.ctfadmin.models import Settings
from .models import Challs;
from ctfadmin.models import Settings


# Create your views here.
def challs(request):
    challs = Challs.objects.filter(active=True)
    settings = Settings.objects.get(id=1)
    chall = {
        "challs": challs,
        "tutorial": 1,
        "user": "Sleipner",
        "settings": settings,
    }
    print(challs)
    return render(request, 'challs.html', chall)

def challs_id(request, id_value):
    challs1 = Challs.objects.filter(active=True)
    challs = Challs.objects.filter(id=id_value)
    settings = Settings.objects.get(id=1)
    chall = {
        "challs_test": challs,
        "challs": challs1,
        "tutorial": 0,
        "user": "Sleipner",
        "settings": settings,
    }
    print(challs1)
    #for entry in challs:
    #    print(challs.id)
    return render(request, 'challs.html', chall)



def dbtest(request):
    challs = Challs.objects.all()
    chall = {
        "challs_test": challs
    }
    return render(request, "bruh.html", chall)
    #return HttpResponse("<h1>{{challs_test}}</h1>", chall)