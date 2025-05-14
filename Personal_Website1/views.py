from django.shortcuts import render
from Talents.models import Talent
from Jobs.models import Job

def home(request):

    Talents = Talent.objects.all()
    Jobs = Job.objects.all()
    return render(request, 'index.html', context={'Talents': Talents, 'Jobs': Jobs})
