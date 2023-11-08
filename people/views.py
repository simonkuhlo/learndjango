from django.shortcuts import render
from .models import Person, Address, Contact

# Create your views here.
def all_people(request):
    return render(request, 'people/all_people.html')

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

