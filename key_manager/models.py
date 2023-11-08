from django.db import models

# Create your models here.

class Adress(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    land = models.CharField(max_length=100)
    area = models.CharField(max_length=100, null=True, default=None)
    description = models.CharField(max_length=500)

    def __str__(self):
        return(str(self.name))

class Person(models.Model):
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Adress, on_delete=models.SET_NULL, null=True, default=None)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', 'created']

    def __str__(self):
        return(str(self.name))


class Key(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Adress, on_delete=models.SET_NULL, null=True, default=None)
    description = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', 'created']

    def __str__(self):
        return(str(self.name))