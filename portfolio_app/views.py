from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from. models import Name, Email, Message
from . forms import ContactForm

# Create your views here.


def index(request):
    """ display page"""
    return render(request, 'portfolio_app/index.html')



def about_me(request):
    """ About me page """
    return render(request, 'portfolio_app/About_me.html')


def Blog(request):
    """ blog posts """
    return render(request, 'portfolio_app/Blog.html')


def contact(request):
    """ contact me page """
    if request.method == 'POST':
        name_contact = request.POST['name-contact']
        email_contact = request.POST['email-contact']
        message_contact = request.POST['message']
        
        # send email to me
        recipients = ['muhammadnurudeen@rocketmail.com']
        send_mail(name_contact, message_contact, email_contact, recipients)
        return render(request, 'portfolio_app/contact.html', {'name_contact': name_contact})    
    else:
        return render(request, 'portfolio_app/contact.html')



def portfolio(request):
    """ display full portfolio """
    return render(request, 'portfolio_app/portfolio.html')

