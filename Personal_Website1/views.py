from django.shortcuts import render
from Talents.models import Talent

def home(request):

    Talents = Talent.objects.all()
    return render(request, 'index.html', context={'Talents': Talents})
