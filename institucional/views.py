from django.shortcuts import render

def home_teste(request):
    return render(request, 'home_teste.html')