from django.forms import ModelForm
from . import models

# Create the form class.
class EditQuestionForm(ModelForm):
    class Meta:
        model = models.Question
        exclude = []


# Creating a form to add an article.
#form = EditQuestionForm()

# Creating a form to change an existing article.
#article = models.Question.objects.get(pk=1)
#form = EditQuestionForm(instance=article)