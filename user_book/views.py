from django.shortcuts import render
from . import entry_handler
# Create your views here.
def home(request):
    return render(request, 'user_book/home.html')

def entry(request, pk):
    entry_dict = entry_handler.entry_to_dict(pk)
    ctx = entry_dict
    return render(request, 'user_book/entry.html', ctx)