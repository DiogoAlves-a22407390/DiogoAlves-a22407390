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