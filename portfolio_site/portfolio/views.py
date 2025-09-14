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
    projetos_ronaud = Projetos_novos.objects.filter(dono='Ronaud').first()
    projetos_iago = Projetos_novos.objects.filter(dono='Iago').first()

    habili_ronaud = Habili_contatos.objects.filter(pessoa = 'Ronaud Andrade').first()
    habili_iago = Habili_contatos.objects.filter(pessoa = 'Iago Rodrigues').first()
    habili_joao = Habili_contatos.objects.filter(pessoa = 'João Gabriel').first()


    context = {
        'projetos_ronaud' : projetos_ronaud, 
        'projetos_iago' : projetos_iago, 

        'habili_ronaud' :  habili_ronaud,
        'habili_iago' : habili_iago,
        'habili_joao' : habili_joao,
    }

    return render(request, 'portfolio/index.html', context)

def form_view(request):
    projetos_ronaud = Projetos_novos.objects.filter(dono='Ronaud').first()
    projetos_iago = Projetos_novos.objects.filter(dono='Iago').first()

    habili_ronaud = Habili_contatos.objects.filter(pessoa = 'Ronaud Andrade').first()
    habili_iago = Habili_contatos.objects.filter(pessoa = 'Iago Rodrigues').first()
    habili_joao = Habili_contatos.objects.filter(pessoa = 'João Gabriel').first()


    context = {
        'projetos_ronaud' : projetos_ronaud, 
        'projetos_iago' : projetos_iago, 

        'habili_ronaud' :  habili_ronaud,
        'habili_iago' : habili_iago,
        'habili_joao' : habili_joao,
    }

    return render(request, 'portfolio/formulario.html', context)