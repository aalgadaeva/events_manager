from django.views.generic import TemplateView
from django.shortcuts import render
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from . import forms


def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Bishmeet!'
        message = 'Your email address has been confirmed - welcome to Bishmeet app, the best online platform to find events near you!'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'success.html', 
            {'recepient': recepient})
    return render(request, 'index.html', {'form':sub})