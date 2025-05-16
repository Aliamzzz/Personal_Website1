from django.shortcuts import render
from ContactMe.models import Contact
from MyProjects.models import Project
from Talents.models import Talent
from Jobs.models import Job

def home(request):

    Talents = Talent.objects.all()
    Jobs = Job.objects.all()
    ContactMe = Contact.objects.all()
    MyProjects = Project.objects.all()
    return render(request, 'index.html', context={'Talents': Talents, 'Jobs': Jobs, 'ContactMe': ContactMe, 'MyProjects': MyProjects})
