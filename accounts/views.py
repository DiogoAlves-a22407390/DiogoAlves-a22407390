from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistoForm

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