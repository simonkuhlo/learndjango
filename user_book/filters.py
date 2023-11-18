from django_filters import FilterSet
from . import models

class InterviewFilter(FilterSet):
    class Meta:
        model = models.Question
        fields = {"interview": ["exact"]}