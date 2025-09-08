from django.shortcuts import render
#from .models import Projetos
# Create your views here.

def home(request):
    context = {
        'nome': 'Ronaud',
        'titulo': 'Meu portfolio',
    }

    return render(request, 'portfolio/home.html', context)
