import django_tables2 as tables
from django_tables2.columns import TemplateColumn
from . import models

class QuestionTable(tables.Table):
    class Meta:
        model = models.Question
        template_name = "django_tables2/bootstrap.html"
        fields = ("sort_id", "name", "question_value", "type", "required", "edit")
    edit = TemplateColumn(template_name='user_book/tables/edit_question_button.html')