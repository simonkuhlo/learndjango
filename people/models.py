from django.db import models

# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    land = models.CharField(max_length=100)
    area = models.CharField(max_length=100, null=True, default=None)
    description = models.CharField(max_length=500, null=True, default=None)

    def __str__(self):
        return(str(self.name))


class Person(models.Model):
    #user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, default=None, blank=True)
    birthday = models.DateField(max_length=100, null=True, default=None)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    email = models.CharField(max_length=100, null=True, default=None, blank=True)
    discord = models.CharField(max_length=100, null=True, default=None, blank=True)
    phone = models.CharField(max_length=100, null=True, default=None, blank=True)
    instagram = models.CharField(max_length=100, null=True, default=None, blank=True)
    twitter = models.CharField(max_length=100, null=True, default=None, blank=True)
    steam = models.CharField(max_length=100, null=True, default=None, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', 'created']

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    

