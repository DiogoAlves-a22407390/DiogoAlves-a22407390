from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()
    creditos = models.IntegerField()
    informacao = models.CharField(max_length=250)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.DecimalField(max_digits=8, decimal_places=0)
    ano = models.IntegerField()
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    formacao_texto = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    unidades_curriculares = models.ManyToManyField('UnidadeCurricular', blank=True)

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200)
    site = models.URLField()
    interesse = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    data_de_realizacao = models.DateField()
    tecnologias = models.ManyToManyField(Tecnologia)
    link = models.URLField()

    def __str__(self):
        return self.titulo


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    professores = models.ManyToManyField(Professor)
    descricao = models.CharField(max_length=200)
    creditos = models.IntegerField()
    imagem = models.ImageField(null=True, blank=True)
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return self.nome


class TFC(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    autor = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    orientador = models.ForeignKey(Professor, on_delete=models.CASCADE)
    ano = models.IntegerField()
    tema = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    nivel = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    experiencia = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_conclusao = models.DateField()
    descricao = models.CharField(max_length=200)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class MakingOF(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    justificacao = models.CharField(max_length=250)
    solucao = models.CharField(max_length=150)
    uso_ia = models.BooleanField()
    descricao_uso_ia = models.CharField(max_length=250)

    def __str__(self):
        return self.tipo