from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'data_de_realizacao', 'tecnologias', 'link']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título do projeto'}),
            'descricao': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descrição'}),
            'data_de_realizacao': forms.DateInput(attrs={'type': 'date'}),
            'tecnologias': forms.CheckboxSelectMultiple(),
            'link': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }


class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome', 'tipo', 'descricao', 'site', 'interesse']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da tecnologia'}),
            'tipo': forms.TextInput(attrs={'placeholder': 'Ex: Framework, Linguagem...'}),
            'descricao': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descrição'}),
            'site': forms.URLInput(attrs={'placeholder': 'https://...'}),
            'interesse': forms.NumberInput(attrs={'min': 0, 'max': 10}),
        }


class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'tipo', 'nivel', 'experiencia', 'projetos']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da competência'}),
            'tipo': forms.TextInput(attrs={'placeholder': 'Ex: Técnica, Soft Skill...'}),
            'nivel': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'experiencia': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'projetos': forms.CheckboxSelectMultiple(),
        }


class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['titulo', 'tipo', 'instituicao', 'data_inicio', 'data_conclusao', 'descricao', 'aluno']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título da formação'}),
            'tipo': forms.TextInput(attrs={'placeholder': 'Ex: Licenciatura, Curso...'}),
            'instituicao': forms.TextInput(attrs={'placeholder': 'Nome da instituição'}),
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_conclusao': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descrição'}),
        }