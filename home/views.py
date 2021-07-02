from django.shortcuts import render, HttpResponse
from home.models import Project,Message
from datetime import datetime
import smtplib

# Create your views here.

'''
def index(request):
    project = Project.objects.all()
    return render(request, 'index.html',{'projects': project})
    #return HttpResponse("Home")
'''

def about(request):
    return HttpResponse("About")

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        Email = request.POST.get('email')
        mymessage = request.POST.get('message')
        # server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        # server.login("noreplydeveloperteam12@gmail.com", "bijuborahkvcut")
        # server.sendmail("noreplydeveloperteam12@gmail.com","bijuborah2017@gmail.com",mymessage)
        # server.quit()
        mes = Message(email=Email , message=mymessage)
        mes.save()
    return render(request, 'contact.html')

def project(request):
    project = Project.objects.all()
    return render(request, 'project.html',{'projects': project})

def cycle(request):
    return render(request, 'cycle.html')

def dogo(request):
    return render(request, 'dogo.html')

def about(request):
    return render(request, 'about.html')

def notfound(request):
    return render(request, 'notfound.html')



