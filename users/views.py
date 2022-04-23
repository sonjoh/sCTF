from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import *
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login

# Create your views here.
def register_account(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        print("POST REQUEST")
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Account created for {username}!')
            form.save()
            return redirect('/challs/')
            
    else:
        form = CreateUserForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def user_login(request):

    if request.method == "POST":
        username = request.POST['lusername']
        password = request.POST['lpassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('<h1>It Works</h1>')
        else:
            return HttpResponse("<h1>It doesnt work</h1>")

    return render(request, 'login.html')