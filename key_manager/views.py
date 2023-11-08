from django.shortcuts import render
from .models import Key

# Create your views here.
def all_keys(request):
    keys = Key.objects.all()
    ctx = {"keys" : keys}
    return render(request, 'key_manager/all_keys.html', ctx)

def single_key(request, pk):
    key = Key.objects.get(id=pk)
    ctx = {'key' : key}
    return render(request, 'key_manager/single_key.html', ctx)