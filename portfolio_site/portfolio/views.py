from django.shortcuts import render
from .models import Projetos_novos
from .models import Habili_contatos
#from .models import Projetos
# Create your views here.

def home(request):
    projetos_ronaud = Projetos_novos.objects.filter(dono='Ronaud')
    projetos_iago = Projetos_novos.objects.filter(dono='Iago')

    habili_ronaud = Habili_contatos.objects.filter(pessoa = 'Ronaud').first()


    context = {
        'projetos_ronaud' : projetos_ronaud, 
        'projetos_iago' : projetos_iago, 
        'habili_ronaud' :  habili_ronaud, 
    }

    return render(request, 'portfolio/home.html', context)


def index(request):
    projetos_ronaud = Projetos_novos.objects.filter(dono='Ronaud')
    projetos_iago = Projetos_novos.objects.filter(dono='Iago')

    habili_ronaud = Habili_contatos.objects.filter(pessoa = 'Ronaud').first()


    context = {
        'projetos_ronaud' : projetos_ronaud, 
        'projetos_iago' : projetos_iago, 
        'habili_ronaud' :  habili_ronaud, 
    }

    return render(request, 'portfolio/index.html', context)