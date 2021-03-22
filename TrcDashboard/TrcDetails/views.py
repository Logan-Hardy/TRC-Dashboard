from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Companionship, Survey, Meeting

def trcDetailsPageView(request) :
    return render(request, 'trcDetails/trcDetails.html')

def TrcDetailsPageView(request, missionary_id) :
    missionaryData = Person.objects.get(pk=missionary_id)
    
    context = {
        "missionaryData" : missionaryData,
    }
    
    return render(request, 'trcDetails/trcDetails.html', context)

# def trcMeetingsPageView(request, missionary_id) :
#     missionary_id = Person.objects.get(id=missionary_id)
#     return render(request, 'trcDetails/trcDetails.html')
    
def summaryPageView(request) :
    # missionary1 = Person(first_name="John", last_name="Smith", gender='M', type="missionary")
    # missionary1.save()   
    # missionary2 = Person(first_name="Mike", last_name="Tyson", gender='M', type="missionary")
    # missionary2.save()
    # missionary3 = Person(first_name="Katelyn", last_name="Carmichael", gender='F', type="missionary")
    # missionary3.save()  
    # missionary4 = Person(first_name="Jori", last_name="Casey", gender='F', type="missionary")
    # missionary4.save()   
    # missionary5 = Person(first_name="Olivia", last_name="Freeman", gender='F', type="missionary")
    # missionary5.save()    
        
    # employee1 = Person(first_name="Quinn", last_name="Johnson", gender='M', type="employee")
    # employee1.save() 
    # employee2 = Person(first_name="Elizabeth", last_name="Nelson", gender='F', type="employee")
    # employee2.save() 

    # actor1 = Person(first_name="Robert", last_name="Allen", gender='M', type="actor")
    # actor1.save() 
    # actor2 = Person(first_name="Danny", last_name="Cutler", gender='F', type="actor")
    # actor2.save() 


    # companionship1 = Companionship(seniorCompanion=missionary1, juniorCompanion=missionary2)
    # companionship1.save()
    # companionship2 = Companionship(seniorCompanion=missionary3, juniorCompanion=missionary4)
    # companionship2.save()
        
    # survey1 = Survey(impression="They did a great job teaching the lesson", feltSpirit=True) 
    # survey1.save()   
        
    # trcMeeting1 = Meeting(survey=survey1, employee=employee1, actor=actor1, companionship=companionship1)
    # trcMeeting1.save()
    # trcMeeting2 = Meeting(survey=survey1, employee=employee2, actor=actor2, companionship=companionship2)
    # trcMeeting2.save()

    return render(request, 'trcDetails/summary.html')

def trcMeetingsPageView(request) :
    return render(request, 'trcDetails/trcMeetings.html')

def viewMissionariesPageView(request) :
    
    missionaryData = Person.objects.filter(type="missionary").order_by('last_name')
    context = {
        "missionaryData" : missionaryData,
    }
    return render(request, 'trcDetails/viewMissionaries.html', context)