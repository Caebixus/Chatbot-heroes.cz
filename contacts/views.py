from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import Contact


# Create your views here.

def contact(request):
    if request.method == 'POST':
        if request.POST['names'] and request.POST['emails'] and request.POST['descriptions']:
            contact = Contact()
            contact.name = request.POST['names']
            contact.email = request.POST['emails']
            contact.phone = request.POST['phones']
            contact.description = request.POST['descriptions']
            contact.save()

            messages.success(request, 'Děkujeme, zpráva byla odeslána')
            return redirect('homepage')
        else:
            messages.success(request, 'Zpráva neodeslána')
            return redirect('homepage')
