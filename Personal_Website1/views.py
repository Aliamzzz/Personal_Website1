from django.shortcuts import render
from ContactMe.models import Contact, Message
from MyProjects.models import Project
from Talents.models import Talent
from Jobs.models import Job

def home(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        Message.objects.create(firstName=firstName, lastName=lastName, email=email, phone=phone, message=message)

    Talents = Talent.objects.all()
    Jobs = Job.objects.all()
    ContactMe = Contact.objects.all()
    MyProjects = Project.objects.all()
    return render(request, 'index.html', context={'Talents': Talents, 'Jobs': Jobs,
                                                  'ContactMe': ContactMe, 'MyProjects': MyProjects})

def contact(request):
    name = request.GET.get('name')
    family = request.GET.get('family')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    message = request.GET.get('message')
    return render(request, 'index.html', context={'name': name, 'family': family,
                                                  'email': email, 'phone': phone, 'message': message})