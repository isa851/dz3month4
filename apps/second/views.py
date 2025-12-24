from django.shortcuts import render
from apps.second.models import Contact
# Create your views here.

def index(request):
    contact = Contact.objects.latest("id")
    return render(request,"index.html",locals())

def contact(request):
    contact = Contact.objects.latest("id")
    return render(request,"contact.html",locals())