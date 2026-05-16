from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistoForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Perfil

# Create your views here.

def login_view(request):
    erro = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('portfolio_index')
        else:
            erro = 'Utilizador ou senha incorretos.'
    return render(request, 'accounts/login.html', {'erro': erro})


def logout_view(request):
    logout(request)
    return redirect('login')


def registo_view(request):
    form = RegistoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'accounts/registo.html', {'form': form})


def envia_email(user, email, link):
    send_mail(
        subject='Portfólio: Autenticação por link mágico',
        message=f'Olá {user.username},\n\nClique no link abaixo para entrar na aplicação:\n\n{link}\n\nEste link é de uso único.',
        from_email='portfolio@gmail.com',
        recipient_list=[email],
    )
 
 
def magic_link_request(request):
    """O utilizador submete o email e recebe um link mágico."""
    mensagem = None
    erro = None
 
    if request.method == 'GET' and 'email' in request.GET:
        email = request.GET.get('email')
 
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
 
            # Gera token e guarda no perfil
            token = secrets.token_urlsafe(32)
            perfil, _ = Perfil.objects.get_or_create(user=user)
            perfil.token = token
            perfil.save()
 
            # Constrói o link com o token no URL
            link = request.build_absolute_uri(f'/accounts/autentica/?token={token}')
 
            envia_email(user, email, link)
            mensagem = f'Link enviado para {email}. Verifica o teu email.'
        else:
            erro = 'Não existe nenhum utilizador com esse email.'
 
    return render(request, 'accounts/magic_link_request.html', {
        'mensagem': mensagem,
        'erro': erro,
    })
 
 
def autentica_magic_link(request):
    """O utilizador clica no link e entra automaticamente."""
    token = request.GET.get('token')
 
    try:
        perfil = Perfil.objects.get(token=token)
        user = perfil.user
 
        # Invalida o token após uso
        perfil.token = None
        perfil.save()
 
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('portfolio_index')
 
    except Perfil.DoesNotExist:
        return render(request, 'accounts/magic_link_invalido.html')
 