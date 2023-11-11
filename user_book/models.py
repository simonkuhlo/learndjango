from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Interview(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
class Entry(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    interview = models.ForeignKey(Interview, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', 'created']

    def __str__(self):
        return(str(self.id))

class Question(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    question_value = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=100) #FileUpload, Interview, AboutMe
    required = models.BooleanField(default=False)

    def __str__(self):
        return(str(self.name))
    
class Answer(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer_value = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return(str(self.answer_value))

