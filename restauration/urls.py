from django.contrib import admin
from django.urls import path, include
from .views import accueil, appéritifs, repas, boulangerie, liste_article, detail_article
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.accueil, name='accueil',),
   path('appéritifs/',views.appéritifs, name='appéritifs', ),
   path('repas/', views.repas, name='repas', ),
   path('boulangerie/', views.boulangerie, name='boulangerie', ),
   path('liste_article/', views.liste_article, name= 'liste_article',),
   path('detail_article/<int:pk>', views.detail_article, name= 'detail_article')

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)