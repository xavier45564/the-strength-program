from django.shortcuts import render
from .models import *
from .forms import *

def home(request):
    return render(request, 'tspapp/index.html')

def about(request):
    return render(request, 'tspapp/about.html')

def appointment(request):
    return render(request, 'tspapp/appointment.html')

def contact(request):
    return render(request, 'tspapp/contact.html')

def services(request):
    return render(request, 'tspapp/services.html')

def teamDetails(request):
    return render(request, 'tspapp/team-details.html')

def team(request):
    return render(request, 'tspapp/team.html')