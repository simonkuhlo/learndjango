from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
import django_tables2 as dtables
from . import models
from . import tables
from . import filters
# Create your views here.

def interview(request, pk):
    question_list = models.Question.objects.filter(interview=pk).order_by('sort_id')
    ctx = {
        "questions" : question_list
        }
    return render(request, 'user_book/admin/interview_viewer.html', ctx)



class interview_manager(SingleTableMixin, FilterView):
    table_class = tables.QuestionTable
    model = models.Question
    template_name = 'user_book/admin/home.html'
    filterset_class = filters.InterviewFilter
