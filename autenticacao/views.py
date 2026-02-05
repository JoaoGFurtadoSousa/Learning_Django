from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
import os

def cadastro(request): 
    pessoa = "Joao"
    return render(request, "cadastro\index.html", {"pessoas": pessoa}) 


def salvar_pessoa_no_banco(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(password)
    usuario = User.objects.create_user(username = nome, email = email, password= password)
    return render(request, 'forms.html')


def lista_todas_as_pessoas(request):
    lista_de_pessoas = User.objects.all()
    return render(request, 'lista_de_pessoas.html', {'pessoas': lista_de_pessoas})

def login(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email != None and password != None:
            usuario = User.objects.get(email= email)
            if usuario:
                password = check_password(usuario.password, password)
                if usuario.password == password:
                    print('boa')
                    return render(request, 'home.html')
    return render(request, 'login.html')

    