 #from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def projet(request):
    return render(request, 'projet.html')

def equipe(request):
    return render(request, 'equipe.html')