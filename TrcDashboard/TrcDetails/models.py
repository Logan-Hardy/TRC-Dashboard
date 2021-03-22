from django.db import models
from datetime import datetime

class Person(models.Model) :
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 1, default='M')
    type = models.CharField(max_length = 15)
    
    def __str__(self) :
        return (self.first_name + ' ' + self.last_name)
    
class Companionship(models.Model) :
    seniorCompanion = models.ForeignKey(Person, related_name="comp_one", on_delete = models.DO_NOTHING)
    juniorCompanion = models.ForeignKey(Person, related_name="comp_two", on_delete = models.DO_NOTHING)
    #trioComp = models.ForeignKey(Person, null = True, related_name="comp_three", on_delete = models.DO_NOTHING)
    
    def __str__(self) :
        return (self.seniorCompanion + ' ' + self.juniorCompanion)
        #return (self.seniorCompanion + ' ' + self.juniorCompanion + ' ' + self.trioComp)

class Survey(models.Model) :
    impression = models.CharField(max_length = 300)
    feltSpirit = models.BooleanField(default=True)
    
    def __str__(self) :
        return (self.impression)

class Meeting(models.Model) :
    startTime = models.DateTimeField(default=datetime.now)
    endTime = models.DateTimeField(default=datetime.now)
    roomNumber = models.IntegerField(default=201)
    survey = models.ForeignKey(Survey, blank = True, null = True, on_delete = models.DO_NOTHING)
    #recording = models.
    employee = models.ForeignKey(Person, related_name="employee", on_delete = models.DO_NOTHING)
    actor = models.ForeignKey(Person, related_name="actor", on_delete = models.DO_NOTHING)
    companionship = models.ForeignKey(Companionship, on_delete = models.DO_NOTHING)
    
    def __str__(self) :
        return (self.startTime + ' ' + self.roomNumber + '' + self.companionship)
        #return (self.actor + ' ' +self.startTime + ' ' + self.roomNumber + '' + self.companionship)
    
    

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

