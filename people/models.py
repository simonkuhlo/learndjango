from django.db import models

# Create your models here.
class Adress(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    land = models.CharField(max_length=100)
    area = models.CharField(max_length=100, null=True, default=None)
    description = models.CharField(max_length=500, null=True, default=None)

    def __str__(self):
        return(str(self.name))


class Contact(models.Model):
    address = models.ForeignKey(Adress, on_delete=models.SET_NULL, null=True, default=None)
    email = models.CharField(max_length=100)
    discord = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    steam = models.CharField(max_length=100)

    def __str__(self):
        return(str(self.id))


class Person(models.Model):
    #user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, default=None)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, default=None)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', 'created']

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    

