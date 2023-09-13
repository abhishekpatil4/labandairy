from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def dashboard(request):
    
    return render(request,'dashboard.html')

def laagAccounts(request):
    return HttpResponse('this is the laag account page')

def extras(request):
    return render(request, "404.html")

 
def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Welcome {username}".format(username=username))
            return redirect('dashboard')
        else:
            messages.error(request, "You are not authorised, please check your credentials and try again later")
            return redirect('login')
    else:
        return render(request, 'login.html') 

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')

def cows(request):
    return HttpResponse('cows page')

def handlecows(request, slug):
    return HttpResponse('handle cows')

def handleLaagAccounts(request, slug):
    return HttpResponse('handle laag accounts page')

def milkrecord(request, slug):
    return HttpResponse('milk record page')

def medication(request, slug):
    return HttpResponse('this is the medication page')

