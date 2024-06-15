from unittest import result
from django.contrib import admin
from django.urls import path

from .views import diabitic,resultl,bloodpressure,recipe,Chicken_on_Sweetcorn_Puree,Easy_cheesy_tuna_baked_potatoes,lemontarragonandpoachedchickensandwich
from .views import lowgibananabread,airfryerroastedvegetablesalad,sweetnsourchicken,figsstuffedwithricottahoneyandwalnuts,simplelemonpeppersalmonforone,spicyorangebarbequepork,bloodglucosw,type1,type2
from .views import bprecipe,grilledegplant,chickprapotato,chickpeaquinoa,veggiesfajita,mushroom,rostedsalmonrice,bpinformation,infromation,familyandcare,kidandteen,symptoms,whentoseedoctor,causes,riskfactor
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
    path('bloodpressure/recipe',bprecipe,name='bprecipe'),
    path('bloodpressure/recipe/grilledeggplant',grilledegplant,name='grilledegplant'),
    path('bloodpressure/recipe/chickprapotato',chickprapotato,name='chickprapotato'),
    path('bloodpressure/recipe/chickpeaquinoa',chickpeaquinoa,name='chickpeaquinoa'),
    path('bloodpressure/recipe/veggiesfajitas',veggiesfajita,name='veggiesfajita'),
    path('bloodpressure/recipe/mushroom',mushroom,name='mushroom'),
    path('bloodpressure/recipe/rostedsalmonrice',rostedsalmonrice,name='rostedsalmonrice'),
    path('bloodpressure/information',bpinformation,name='bpinformation'),
    path('diabetic/information',infromation,name='information'),
    path('diabetic/familyandcare',familyandcare,name='information1'),
    path('diabetic/kidandteen',kidandteen,name='information2'),
    path('bloodpressure/symptoms',symptoms,name='symptoms'),
    path('bloodpressure/whentoseedoctor',whentoseedoctor,name='whentoseedoctor'),
    path('bloodpressure/causes',causes,name='causes'),
    path('bloodpressure/riskfactor',riskfactor,name='riskfactor'),
    path('diabetic/bloodglucosemonitoring',bloodglucosw,name='bloodglucows'),
    path('diabetic/type1',type1,name='type1'),
    path('diabetic/type2',type2,name='type2'),

]
