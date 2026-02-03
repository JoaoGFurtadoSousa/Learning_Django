from django.shortcuts import render
# Create your views here.


def cadastro(request): 
    pessoa = [{"nome": "John Snow",
               "idade": 22},
               {"nome": "Jofrey",
               "idade": 18},
               {"nome": "Jorah",
               "idade": 55}]
    return render(request, "cadastro\index.html", {"pessoas": pessoa}) 