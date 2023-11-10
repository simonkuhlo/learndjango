from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.apps import apps as apps
from .forms import SearchForm

def home(request):
    return render(request, 'applist.html')

def search(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        search_query = request.POST["search"]
        models = apps.get_models(include_auto_created=True, include_swapped=True)
        for model in models:
            model.objects.filter(name__contains="Terry")
    
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, "name.html", {"form": form})