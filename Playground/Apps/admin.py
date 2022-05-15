from django.contrib import admin

from person.models import person
from .models import person

admin.site.register(person)

# Register your models here.
