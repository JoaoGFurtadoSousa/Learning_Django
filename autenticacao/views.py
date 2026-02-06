from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
import os

def cadastro(request): 
    pessoa = "Joao"
    return render(request, "cadastro\index.html", {"pessoas": pessoa}) 


def salvar_pessoa_no_banco(request):
    if request.POST:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)
        usuario = User.objects.create_user(username = nome, email = email, password= password)
        return render(request, 'login.html')
    return render(request, 'forms.html')

def lista_todas_as_pessoas(request):
    lista_de_pessoas = User.objects.all()
    return render(request, 'lista_de_pessoas.html', {'pessoas': lista_de_pessoas})

def login(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email != None and password != None:
            try:
                usuario = User.objects.get(email= email)
                print(password)
                print(usuario.password)
                print(f'Senha digitada: {password}')
                if check_password(password, usuario.password) == True:
                    print(f'entrou: {usuario.password}')
                    return render(request, 'home.html')
                print('senha incorreta')
                return render(request, 'login.html')
            except User.DoesNotExist:
                return HttpResponse({'error':'User not found'}, status= 404)
        
    else:
        print('Requisicao do GET')
        return render(request, 'login.html') 

