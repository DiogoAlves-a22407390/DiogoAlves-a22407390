from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='portfolio_index'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('alunos/', views.alunos_view, name='alunos'),
    path('professores/', views.professores_view, name='professores'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('unidades-curriculares/', views.unidades_curriculares_view, name='unidades_curriculares'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('makingof/', views.makingof_view, name='makingof'),
]