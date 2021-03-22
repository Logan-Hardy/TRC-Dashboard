from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
# from django.contrib.auth import logout
#from trcDetails.models import Person, Companionship, Survey, Meeting

def indexPageView(request) :
    return render(request, 'index/index.html')

def homePageView(request) :
    return render(request, 'index/home.html')

def logoutPageView(request) :
    return render(request, 'index/logout.html')

def logout(request):
    auth.logout(request)
    return render(request,'index/logout.html')
