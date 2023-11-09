from django.shortcuts import render
from .models import Person, Address, Contact

# Create your views here.
def people_list(request):
    people = Person.objects.all()
    ctx = {"people" : people}
    return render(request, 'people/people_list.html', ctx)

def address_list(request):
    return render(request, 'people/address_list.html')

def contact_list(request):
    return render(request, 'people/contact_list.html')

def person(request, pk):
    object = Person.objects.get(id=pk)
    ctx = {'person' : object}
    return render(request, 'people/person.html', ctx)

def adress(request, pk):
    object = Address.objects.get(id=pk)
    ctx = {'address' : object}
    return render(request, 'people/address.html', ctx)

def contact(request, pk):
    object = Contact.objects.get(id=pk)
    ctx = {'contact' : object}
    return render(request, 'people/contact.html', ctx)

