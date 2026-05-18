from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm, RegistoAutorForm


def is_autor(user):
    return user.is_authenticated and (
        user.groups.filter(name='autores').exists() or user.is_superuser
    )


# ---------- Listagem de artigos ----------

def artigos_view(request):
    artigos = Artigo.objects.select_related('autor').prefetch_related('likes').order_by('-data_criacao')
    return render(request, 'artigos/artigos.html', {
        'artigos': artigos,
        'is_autor': is_autor(request.user),
    })


# ---------- Detalhe de artigo ----------

def artigo_view(request, id):
    artigo = get_object_or_404(Artigo.objects.prefetch_related('comentarios__autor', 'likes'), pk=id)
    comentarios = artigo.comentarios.order_by('-data_criacao')
    form_comentario = ComentarioForm()

    if request.method == 'POST' and request.user.is_authenticated:
        if 'comentario' in request.POST:  # ← distingue o form de comentário
            form_comentario = ComentarioForm(request.POST)
            if form_comentario.is_valid():
                comentario = form_comentario.save(commit=False)
                comentario.artigo = artigo
                comentario.autor = request.user
                comentario.save()
                return redirect('artigo', id=artigo.id)

    ja_gostou = request.user in artigo.likes.all() if request.user.is_authenticated else False

    return render(request, 'artigos/artigo.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
        'ja_gostou': ja_gostou,
        'is_autor': is_autor(request.user),
        'e_meu': artigo.autor == request.user,
    })
    

# ---------- Like ----------

@login_required
def like_view(request, id):
    if request.method == 'POST':
        artigo = get_object_or_404(Artigo, pk=id)
        if request.user in artigo.likes.all():
            artigo.likes.remove(request.user)
        else:
            artigo.likes.add(request.user)
    return redirect('artigo', id=id)


# ---------- Criar artigo ----------

@login_required
def artigo_create(request):
    if not is_autor(request.user):
        return redirect('artigos')
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect('artigos')
    return render(request, 'artigos/form.html', {
        'form': form,
        'titulo': 'Novo Artigo',
    })


# ---------- Editar artigo ----------

@login_required
def artigo_edit(request, id):
    artigo = get_object_or_404(Artigo, pk=id)
    # Só o autor do artigo pode editar
    if request.user != artigo.autor and not request.user.is_superuser:
        return redirect('artigos')
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigo', id=artigo.id)
    return render(request, 'artigos/form.html', {
        'form': form,
        'titulo': f'Editar: {artigo.titulo}',
    })


# ---------- Apagar artigo ----------

@login_required
def artigo_delete(request, id):
    artigo = get_object_or_404(Artigo, pk=id)
    if request.user != artigo.autor and not request.user.is_superuser:
        return redirect('artigos')
    artigo.delete()
    return redirect('artigos')


# ---------- Registo de autor ----------

def registo_autor_view(request):
    form = RegistoAutorForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        # Associa automaticamente ao grupo autores
        grupo_autores, _ = Group.objects.get_or_create(name='autores')
        user.groups.add(grupo_autores)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('artigos')
    return render(request, 'artigos/registo_autor.html', {'form': form})