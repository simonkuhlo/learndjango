from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
import django_tables2 as dtables
from . import models
from . import tables
from . import filters
from . import forms
# Create your views here.

def edit_question(request, pk):
    question = models.Question.objects.get(id=pk)
    form = forms.EditQuestionForm(instance=question)
    ctx = {
        "form" : form
        }
    return render(request, 'user_book/admin/edit_question.html', ctx)

class interview_manager(SingleTableMixin, FilterView):
    table_class = tables.QuestionTable
    model = models.Question
    template_name = 'user_book/admin/home.html'
    filterset_class = filters.InterviewFilter

#new concept
class question_list(SingleTableMixin, FilterView):
    pass

def add_question(request, id):
    pass

def edit_question(request, id):
    pass

def delete_question(request, id):
    pass

#approach 2
def list_object(request, type):
    match type:

        case "question" : pass

        case "interview" : pass

        case "" : pass