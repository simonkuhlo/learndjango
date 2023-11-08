from django.shortcuts import render
from .models import Key

# Create your views here.
def test(request):
    keys = Key.objects.all()
    ctx = {"keys" : keys}
    return render(request, 'key_manager/test.html', ctx)