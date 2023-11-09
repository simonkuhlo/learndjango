from django.shortcuts import render
from .models import Person, Address

# Create your views here.
def people_list(request):
    people = Person.objects.all()
    ctx = {"people" : people}
    return render(request, 'people/people_list.html', ctx)

def address_list(request):
    people = Person.objects.all()
    ctx = {"people" : people}
    return render(request, 'people/people_list.html', ctx)

def person(request, pk):
    object = Person.objects.get(id=pk)
    ctx = {'person' : object}
    return render(request, 'people/person.html', ctx)

def adress(request, pk):
    object = Address.objects.get(id=pk)
    ctx = {'address' : object}
    return render(request, 'people/address.html', ctx)

