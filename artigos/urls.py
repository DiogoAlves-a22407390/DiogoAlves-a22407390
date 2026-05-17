from django.urls import path
from . import views

urlpatterns = [
    path('', views.artigos_view, name='artigos'),
    path('<int:id>/', views.artigo_view, name='artigo'),
    path('<int:id>/like/', views.like_view, name='like'),
    path('novo/', views.artigo_create, name='artigo_create'),
    path('<int:id>/editar/', views.artigo_edit, name='artigo_edit'),
    path('<int:id>/apagar/', views.artigo_delete, name='artigo_delete'),
    path('registo/', views.registo_autor_view, name='registo_autor'),
]