from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def localizacao(request):
    return render(request, 'localizacao.html')