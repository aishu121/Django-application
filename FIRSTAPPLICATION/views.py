from django.shortcuts import render
from .models import Name, ID, Contact, Address

# Create your views here.
def index(request):
    name = Name.objects.all()
    ids = ID.objects.all()
    contact = Contact.objects.all()
    address = Address.objects.all()
    return render(request,'index.html',{
        'name': name,
        'id': ids,
        'contact': contact,
        'adress': address
    })

