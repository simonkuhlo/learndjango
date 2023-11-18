from django.shortcuts import render
from . import entry_handler
from . import models
# Create your views here.

def interview(request, pk):
    question_list = models.Question.objects.filter(interview=pk).order_by('sort_id')
    ctx = {
        "questions" : question_list
        }
    return render(request, 'user_book/admin/interview_viewer.html', ctx)
