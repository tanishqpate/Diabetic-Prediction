from unittest import result
from django.contrib import admin
from django.urls import path

from .views import diabitic,resultl,bloodpressure,recipe,Chicken_on_Sweetcorn_Puree,Easy_cheesy_tuna_baked_potatoes,lemontarragonandpoachedchickensandwich
from .views import lowgibananabread,airfryerroastedvegetablesalad,sweetnsourchicken,figsstuffedwithricottahoneyandwalnuts,simplelemonpeppersalmonforone,spicyorangebarbequepork
urlpatterns = [
    path("diabetic/",diabitic,name='diabetic'),
    path("result/",resultl,name='result'),
    path("bloodpressure/",bloodpressure,name='bloodpressure'),
    path("diabetic/recipe",recipe,name='recipe'),
    path("diabetic/recipe/ChickenonSweetcornPuree",Chicken_on_Sweetcorn_Puree,name='Chicken_on_Sweetcorn_Puree'),
    path("diabetic/recipe/cheesytunabakedpotatoes",Easy_cheesy_tuna_baked_potatoes,name="Easy_cheesy_tuna_baked_potatoes"),
    path("diabetic/recipe/lowgibananabread",lowgibananabread,name='lowgibananabread'),
    path('diabetic/recipe/airfryerroastedvegetablesalad',airfryerroastedvegetablesalad,name='airfryerroastedvegetablesalad'),
    path('diabetic/recipe/sweetnsourchicken',sweetnsourchicken,name='sweetnsourchicken'),
    path('diabetic/recipe/figsstuffedwithricottahoneyandwalnuts',figsstuffedwithricottahoneyandwalnuts,name='figsstuffedwithricottahoneyandwalnuts'),
    path('diabetic/recipe/simplelemonpeppersalmonforone',simplelemonpeppersalmonforone,name='simplelemonpeppersalmonforone'),
    path('diabetic/recipe/lemontarragonandpoachedchickensandwich',lemontarragonandpoachedchickensandwich,name='lemontarragonandpoachedchickensandwich'),
    path('diabetic/recipe/spicyorangebarbequepork',spicyorangebarbequepork,name='spicyorangebarbequepork'),


]
