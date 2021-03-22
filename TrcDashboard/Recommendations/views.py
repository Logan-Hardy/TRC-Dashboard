from django.shortcuts import render
from django.http import HttpResponse
# from trcDetails.models import Person, Companionship, Survey, Meeting

def recommendationsPageView(request) :
    return render(request, 'recommendations/recommendations.html')