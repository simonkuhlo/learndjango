from django.shortcuts import render
from .handlers import entry_handler
from . import models
# Create your views here.
def home(request):
    return render(request, 'user_book/home.html')

def entry(request, pk):
    entry_dict = entry_handler.entry_to_dict(pk)
    ctx = entry_dict
    return render(request, 'user_book/entry.html', ctx)

def interview(request, pk):
    question_list = models.Question.objects.filter(interview=pk).order_by('sort_id')
    ctx = {
        "questions" : question_list
        }
    return render(request, 'user_book/new_entry.html', ctx)

