from django.contrib import admin
from django.urls import path, include
from .views import accueil, appéritifs, repas, boulangerie
from .import views

urlpatterns = [
   path('', views.accueil, name='accueil',),
   path('appéritifs/',views.appéritifs, name='appéritifs', ),
   path('repas/', views.repas, name='repas', ),
   path('boulangerie/', views.boulangerie, name='boulangerie', ),

    
]
