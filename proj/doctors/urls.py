from unittest import result
from django.contrib import admin
from django.urls import path

from .views import diabitic,resultl,bloodpressure,recipe,recipe1

urlpatterns = [
    path("diabitic/",diabitic,name='diabitic'),
    path("result/",resultl,name='result'),
    path("bloodpressure/",bloodpressure,name='bloodpressure'),
    path("diabitic/recipe",recipe,name='recipe'),
     path("diabitic/recipe1",recipe1,name='recipe1'),
    


 
]
