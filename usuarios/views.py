from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User, auth
from django.urls import reverse
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/cadastro')

        # TO DO: validar força da senha

        user = User.objects.filter(username=username)

        if user:
            messages.add_message(request, constants.ERROR, 'Este usuário já existe')
            return redirect(reverse('cadastro'))

        try:
            user = User.objects.create_user(username=username, email=email)
            user.set_password(senha)
            user.save()

            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
            return redirect('/login')
        except:
            messages.add_message(request, constants.WARNING, 'Erro interno do sistema')
            return redirect('/cadastro')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect(reverse('login'))

        auth.login(request, user)
        return redirect('/novo_evento')
