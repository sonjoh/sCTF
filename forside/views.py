from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', { 'name': 'Sleipner'})

def forside(request):
    return render(request, 'forside.html')
