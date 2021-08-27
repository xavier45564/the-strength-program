import smtplib
from django.shortcuts import render
from django.utils.cache import add_never_cache_headers
from email.message import EmailMessage
from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import redirect
from datetime import datetime

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "blueautomessenger@gmail.com"
    msg['from'] = user
    password = "szacnegtzcotgqma"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

date = datetime.now().strftime('%Y/%m/%d %H:%M')


def home(request):
    form = NewsletterForm()
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            contact.instance.date = date
            email = form.cleaned_data['email']
            amount = Newsletter.objects.count() + 1
            body = 'User with this email requested to join your news letter \n' + email + '\n' + 'Newspaper Participants: ' + str(amount)
            email_alert('New Newsletter Request! \n', body, 'info@thestrengthprogram.org')
            form.save()
            return redirect('/')
    currentYear = datetime.now().year
    context = {
        'form': form,
        'year': currentYear,
    } 
    return render(request, 'tspapp/index.html', context)

def about(request):
    form = NewsletterForm()
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.instance.date = date
            email = form.cleaned_data['email']
            amount = Newsletter.objects.count() + 1
            body = 'User with this email requested to join your news letter \n' + email + '\n' + 'Newspaper Participants: ' + str(amount)
            email_alert('New Newsletter Request! \n', body, 'info@thestrengthprogram.org')
            form.save()
            return redirect('/')
    currentYear = datetime.now().year
    context = {
        'form': form,
        'year': currentYear,
    } 
    return render(request, 'tspapp/about.html', context)

def appointment(request):
    return render(request, 'tspapp/appointment.html')

def contact(request):
    form = NewsletterForm()
    contact = ContactForm()
    contactID = Resume.objects.count()

    if request.method == 'POST' and 'btnform1' in request.POST:
        contact = ContactForm(request.POST, request.FILES)
        if contact.is_valid():
            contact.instance.date = date
            email = contact.cleaned_data['email']
            contact.save()
            body = 'New Resume Upload Follow This Link' + '\n' + 'http://127.0.0.1:8000/admin/website/contact/' + str(contactID) +'/change/'
            email_alert('Resume', body, 'info@thestrengthprogram.org')
            return redirect('/resume')
        
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            contact.instance.date = date
            email = form.cleaned_data['email']
            amount = Newsletter.objects.count() + 1
            body = 'User with this email requested to join your news letter \n' + email + '\n' + 'Newspaper Participants: ' + str(amount)
            email_alert('New Newsletter Request! \n', body, 'info@thestrengthprogram.org')
            form.save()
            return redirect('/')
    currentYear = datetime.now().year
    context = {
        'form': form,
        'year': currentYear,
        'contact': contact,
    } 

    return render(request, 'tspapp/contact.html', context)

def services(request):
    form = NewsletterForm()
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            contact.instance.date = date
            email = form.cleaned_data['email']
            amount = Newsletter.objects.count() + 1
            body = 'User with this email requested to join your news letter \n' + email + '\n' + 'Newspaper Participants: ' + str(amount)
            email_alert('New Newsletter Request! \n', body, 'info@thestrengthprogram.org')
            form.save()
            return redirect('/')
    currentYear = datetime.now().year
    context = {
        'form': form,
        'year': currentYear,
    } 
    return render(request, 'tspapp/services.html', context)

def teamDetails(request):
    return render(request, 'tspapp/team-details.html')

def team(request):
    return render(request, 'tspapp/team.html')