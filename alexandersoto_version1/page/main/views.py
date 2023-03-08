from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
import requests
from django.contrib import messages

def home(request):
    return render(request, 'main/home.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['johann.96@hotmail.com']
            messages.success(request,"Mensaje enviado correctamente") 
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)     
            except BadHeaderError:
                return HttpResponse('invalid header found')
              
             
    return render(request, 'main/contact.html', {'form': form})

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')
