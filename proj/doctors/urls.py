from unittest import result
from django.contrib import admin
from django.urls import path

from .views import diabitic,resultl,bloodpressure,recipe,Chicken_on_Sweetcorn_Puree

urlpatterns = [
    path("diabitic/",diabitic,name='diabitic'),
    path("result/",resultl,name='result'),
    path("bloodpressure/",bloodpressure,name='bloodpressure'),
    path("diabitic/recipe",recipe,name='recipe'),
     path("diabitic/recipe/ChickenonSweetcornPuree",Chicken_on_Sweetcorn_Puree,name='Chicken_on_Sweetcorn_Puree'),
    
 
]
