from django.contrib import admin

# Register your models here.
from .models import Key, Person, Adress

admin.site.register(Key)
admin.site.register(Person)
admin.site.register(Adress)
