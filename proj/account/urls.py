from unittest import result
from django.contrib import admin
from django.urls import path

from .views import Login,signup 

urlpatterns = [

    path('login/',Login,name='login'),
    path('home/',signup,name='Signup'),
    
 
]
