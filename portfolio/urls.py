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

    # Projetos CRUD
    path('projetos/', views.projetos_view, name='projetos'),
    path('projetos/novo/', views.projeto_create, name='projeto_create'),
    path('projetos/<int:id>/editar/', views.projeto_edit, name='projeto_edit'),
    path('projetos/<int:id>/apagar/', views.projeto_delete, name='projeto_delete'),
 
    # Tecnologias CRUD
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologias/nova/', views.tecnologia_create, name='tecnologia_create'),
    path('tecnologias/<int:id>/editar/', views.tecnologia_edit, name='tecnologia_edit'),
    path('tecnologias/<int:id>/apagar/', views.tecnologia_delete, name='tecnologia_delete'),
 
    # Competências CRUD
    path('competencias/', views.competencias_view, name='competencias'),
    path('competencias/nova/', views.competencia_create, name='competencia_create'),
    path('competencias/<int:id>/editar/', views.competencia_edit, name='competencia_edit'),
    path('competencias/<int:id>/apagar/', views.competencia_delete, name='competencia_delete'),
 
    # Formações CRUD
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('formacoes/nova/', views.formacao_create, name='formacao_create'),
    path('formacoes/<int:id>/editar/', views.formacao_edit, name='formacao_edit'),
    path('formacoes/<int:id>/apagar/', views.formacao_delete, name='formacao_delete'),
    
    
    path('sobre/', views.sobre_view, name='sobre'),
]