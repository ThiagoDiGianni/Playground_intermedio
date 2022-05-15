
from django.contrib import admin
from django.urls import path, include
from person.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', include("person.urls")),
        
    
]
