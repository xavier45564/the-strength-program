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
    return render(request, 'tspapp/index.html')

def about(request):
    return render(request, 'tspapp/about.html')

def appointment(request):
    return render(request, 'tspapp/appointment.html')

def contact(request):
    form = NewsletterForm()
    contact = ContactForm()

    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.instance.date = date
            name = contact.cleaned_data['name']
            email = contact.cleaned_data['email']
            dxCode = contact.cleaned_data['dxCode']
            phone = contact.cleaned_data['phone']
            agency = contact.cleaned_data['agency']
            message = contact.cleaned_data['message']
            body = 'Name: ' + name + '\n' + 'Email: ' + email + '\n' + 'DX Code' + dxCode + '\n' + 'Address Phone' + str(phone) + '\n' + 'Message: \n' + message
            email_alert(agency, body, 'sabreexavier@gmail.com')
            contact.save()
            return redirect('/contact')
        
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            contact.instance.date = date
            email = form.cleaned_data['email']
            amount = Newsletter.objects.count() + 1
            body = 'User with this email requested to join your news letter \n' + email + '\n' + 'Newspaper Participants: ' + str(amount)
            email_alert('New Newsletter Request! \n', body, 'sabreexavier@gmail.com')
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
    return render(request, 'tspapp/services.html')

def teamDetails(request):
    return render(request, 'tspapp/team-details.html')

def team(request):
    return render(request, 'tspapp/team.html')