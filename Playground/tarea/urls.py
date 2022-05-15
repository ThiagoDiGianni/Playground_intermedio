
from django.contrib import admin
from django.urls import path, include
from person.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('persona',list_person),
    path('modelos', papa),
    
]
