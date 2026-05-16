from django.shortcuts import render
from .models import (
    Licenciatura, Aluno, Professor, Tecnologia,
    Projeto, UnidadeCurricular, TFC, Competencia, Formacao, MakingOF
)


def index_view(request):
    return render(request, 'portfolio/index.html')


def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})


def alunos_view(request):
    alunos = Aluno.objects.select_related('licenciatura').all()
    return render(request, 'portfolio/alunos.html', {'alunos': alunos})


def professores_view(request):
    professores = Professor.objects.prefetch_related('unidades_curriculares').all()
    return render(request, 'portfolio/professores.html', {'professores': professores})


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})


def projetos_view(request):
    projetos = Projeto.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})


def unidades_curriculares_view(request):
    ucs = UnidadeCurricular.objects.prefetch_related('professores', 'projetos').all()
    return render(request, 'portfolio/unidades_curriculares.html', {'ucs': ucs})


def tfcs_view(request):
    tfcs = TFC.objects.select_related('autor', 'orientador').all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})


def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('projetos').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})


def formacoes_view(request):
    formacoes = Formacao.objects.select_related('aluno').all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})


def makingof_view(request):
    makingof = MakingOF.objects.all()
    return render(request, 'portfolio/makingof.html', {'makingof': makingof})

from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    Licenciatura, Aluno, Professor, Tecnologia,
    Projeto, UnidadeCurricular, TFC, Competencia, Formacao, MakingOF
)
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm


# ---------- Páginas de listagem simples ----------

def index_view(request):
    return render(request, 'portfolio/index.html')


def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})


def alunos_view(request):
    alunos = Aluno.objects.select_related('licenciatura').all()
    return render(request, 'portfolio/alunos.html', {'alunos': alunos})


def professores_view(request):
    professores = Professor.objects.prefetch_related('unidades_curriculares').all()
    return render(request, 'portfolio/professores.html', {'professores': professores})


def unidades_curriculares_view(request):
    ucs = UnidadeCurricular.objects.prefetch_related('professores', 'projetos').all()
    return render(request, 'portfolio/unidades_curriculares.html', {'ucs': ucs})


def tfcs_view(request):
    tfcs = TFC.objects.select_related('autor', 'orientador').all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})


def makingof_view(request):
    makingof = MakingOF.objects.all()
    return render(request, 'portfolio/makingof.html', {'makingof': makingof})


# ---------- Projetos CRUD ----------

def projetos_view(request):
    projetos = Projeto.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})


def projeto_create(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/form.html', {
        'form': form, 'titulo': 'Novo Projeto', 'cancelar_url': 'projetos'
    })


def projeto_edit(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    form = ProjetoForm(request.POST or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    return render(request, 'portfolio/form.html', {
        'form': form, 'titulo': f'Editar Projeto: {projeto.titulo}', 'cancelar_url': 'projetos'
    })


def projeto_delete(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    projeto.delete()
    return redirect('projetos')


# ---------- Tecnologias CRUD ----------

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {
        'tecnologias': tecnologias,
        'gestor': is_gestor(request.user) if request.user.is_authenticated else False,
    })


def tecnologia_create(request):
    form = TecnologiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/form.html', {
        'form': form, 'titulo': 'Nova Tecnologia', 'cancelar_url': 'tecnologias'
    })


def tecnologia_edit(request, id):
    tecnologia = get_object_or_404(Tecnologia, pk=id)
    form = TecnologiaForm(request.POST or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('tecnologias')
    return render(request, 'portfolio/form.html', {
        'form': form, 'titulo': f'Editar Tecnologia: {tecnologia.nome}', 'cancelar_url': 'tecnologias'
    })


def tecnologia_delete(request, id):
    tecnologia = get_object_or_404(Tecnologia, pk=id)
    tecnologia.delete()
    return redirect('tecnologias')


# ---------- Competências CRUD ----------

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('projetos').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})


def competencia_create(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/form.html', {
        'form': form, 'titulo': 'Nova Competência', 'cancelar_url': 'competencias'
    })


def competencia_edit(request, id):
    competencia = get_object_or_404(Competencia, pk=id)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    return render(request, 'portfolio/form.html', {
        'form': form, 'titulo': f'Editar Competência: {competencia.nome}', 'cancelar_url': 'competencias'
    })


def competencia_delete(request, id):
    competencia = get_object_or_404(Competencia, pk=id)
    competencia.delete()
    return redirect('competencias')


# ---------- Formações CRUD ----------

def formacoes_view(request):
    formacoes = Formacao.objects.select_related('aluno').all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})


def formacao_create(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/form.html', {
        'form': form, 'titulo': 'Nova Formação', 'cancelar_url': 'formacoes'
    })


def formacao_edit(request, id):
    formacao = get_object_or_404(Formacao, pk=id)
    form = FormacaoForm(request.POST or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    return render(request, 'portfolio/form.html', {
        'form': form, 'titulo': f'Editar Formação: {formacao.titulo}', 'cancelar_url': 'formacoes'
    })


def formacao_delete(request, id):
    formacao = get_object_or_404(Formacao, pk=id)
    formacao.delete()
    return redirect('formacoes')


def sobre_view(request):
    from itertools import groupby
    from .models import Tecnologia, MakingOF

    tecnologias = Tecnologia.objects.all().order_by('tipo')
    makingof = MakingOF.objects.all()

    # Agrupa tecnologias por tipo
    tecnologias_por_tipo = {}
    for tec in tecnologias:
        if tec.tipo not in tecnologias_por_tipo:
            tecnologias_por_tipo[tec.tipo] = []
        tecnologias_por_tipo[tec.tipo].append(tec)

    return render(request, 'portfolio/sobre.html', {
        'tecnologias_por_tipo': tecnologias_por_tipo,
        'makingof': makingof,
    })

def is_gestor(user):
    return user.groups.filter(name='gestor-portfolio').exists()