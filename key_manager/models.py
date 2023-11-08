from django.db import models
from people import models as people
# Create your models here.

class Key(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(people.Address, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    description = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', 'created']

    def __str__(self):
        return(str(self.name))