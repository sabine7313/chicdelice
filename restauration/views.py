from django.shortcuts import render, redirect
from .models import Article
from .form import FormulaireNewsletter


# Create your views here.
def accueil(request):
    form = FormulaireNewsletter()
    if request.method == 'POST':
        form = FormulaireNewsletter(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')

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