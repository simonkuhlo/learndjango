from django.shortcuts import render
from . import entry_handler
# Create your views here.
def home(request):
    return render(request, 'user_book/home.html')

def entry(request):
    entry = {
        "question_1" : {
            "question" : "question",
            "answer" : "answer"
        }
    }
    ctx = {
        {"entry" : entry}
    }
    return render(request, 'user_book/home.html')

def test(request):
    entry_handler.entry_to_dict(1)
    return render(request, 'user_book/window.html')