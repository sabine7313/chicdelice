from django.shortcuts import render
from .models import Article


# Create your views here.
def accueil (request):
    return render(request, 'page_accueil.html')

def appéritifs (request):
    return render(request, 'appéritifs.html')

def repas(request):
    return render(request, 'repas.html')

def boulangerie(request):
    return render(request, 'boulangerie.html')

def liste_article(request):
    tout_les_articles = Article.objects.all()
    return render(request, 'liste_article.html', locals())

def detail_article(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'detail_article.html',locals())