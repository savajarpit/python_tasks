from django.shortcuts import render,redirect
from datetime import datetime
from .models import Contact
#function for getTime
def get_currentTime():
    return datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
#function home
def home(request):
    currentTime=get_currentTime()
    context={
        "currentTime":currentTime
    }
    return render(request, 'Home.html',context)
#function for collect data from user
def contact(request):
    submitted_data = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contact(name=name, email=email)
        contact.save()
        submitted_data = {'name': name, 'email': email}
    return render(request, 'Home.html', {'submitted_data': submitted_data})
#function for showdata
def allUsers(request):
    users=Contact.objects.all()
    return render(request,"userinfo.html",{"users":users})
#About function
def about(request):
    return render(request,"about.html")