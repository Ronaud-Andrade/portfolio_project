from django.shortcuts import render
from .models import Projetos_novos
#from .models import Projetos
# Create your views here.

def home(request):
    projetos_ronaud = Projetos_novos.objects.filter(dono='Ronaud')
    projetos_iago = Projetos_novos.objects.filter(dono='Iago')

    context = {
        'projetos_ronaud' : projetos_ronaud, 'projetos_iago' : projetos_iago
    }

    return render(request, 'portfolio/home.html', context)
