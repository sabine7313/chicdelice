from django.shortcuts import render



# Create your views here.
def accueil (request):
    return render(request, 'page_accueil.html')

def appéritifs (request):
    return render(request, 'appéritifs.html')

def repas(request):
    return render(request, 'repas.html')

def boulangerie(request):
    return render(request, 'boulangerie.html')