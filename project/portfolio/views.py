from django.shortcuts import redirect, render
from .models import Tecnologia, Projeto, Licenciatura, Docente,Cadeira,Formacao,AreaTematica,TFC
from .forms import ProjetoForm, TecnologiaForm

# Create your views here.

def licenciatura_view(request):
    Licenciaturas = Licenciatura.objects.all()

    return render(request, 'portfolio/licenciatura.html',{'licenciatura': Licenciaturas})

def docentes_view(request):
    Docentes = Docente.objects.all()

    return render(request, 'portfolio/docentes.html', {'docentes': Docentes})

def cadeiras_view(request):
    Cadeiras = Cadeira.objects.all()

    return render(request, 'portfolio/cadeiras.html', {'cadeiras': Cadeiras})

def formacoes_view(request):
    Formacoes = Formacao.objects.all()

    return render(request, 'portfolio/formacoes.html', {'formacoes': Formacoes})

def areaTematica_view(request):
    areaTematica = AreaTematica.objects.all()

    return render(request, 'portfolio/area_tematica.html', {'area_tematica': areaTematica})

def tfcs_view(request):
    tfcs = TFC.objects.all()

    return render(request,'portfolio/tfc.html',{'tfcs':tfcs})


def tecnologias_view(request):
    Tecnologias = Tecnologia.objects.all()

    return render(request, 'portfolio/tecnologias.html',{'tecnologias': Tecnologias})

def novo_tecnologia_view(request):
    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido. 
    # Senão, o form não tem dados e não é válido
    form = TecnologiaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_tecnologia.html', context)

    #form = TecnologiaForm()      # form é uma instancia de ProjetoForm,
                            # formulário em branco com os campos de Projeto

    #context = {'form': form}
    #return render(request, 'portfolio/novo_tecnologia.html', context)

def edita_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    
    if request.POST:
        form = TecnologiaForm(request.POST or None, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)  # cria formulário com dados da instância autor
        
    context = {'form': form, 'tecnologia':tecnologia}
    return render(request, 'portfolio/edita_tecnologia.html', context)

def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    tecnologia.delete()
    return redirect('tecnologias')



def projetos_view(request):
    Projetos = Projeto.objects.all()

    return render(request, 'portfolio/projetos.html',{'projetos': Projetos})

def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES)  
    if form.is_valid():
        form.save()
        return redirect('projetos')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_projeto.html', context)

def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    
    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = TecnologiaForm(instance=projeto)
        
    context = {'form': form, 'projeto':projeto}
    return render(request, 'portfolio/edita_projeto.html', context)

def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('projeto')