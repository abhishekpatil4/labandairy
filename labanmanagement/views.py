from django.shortcuts import render, HttpResponse


def dashboard(request):
    return render(request,'dashboard.html')

def laagAccounts(request):
    return HttpResponse('this is the laag account page')

def extras(request):
    return HttpResponse('this is the extras page')

def handlelogin(request):
    return render(request, 'login.html')

def handlelogout(request):
    return HttpResponse('logout page')

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

