from django.shortcuts import render
# Create your views here.
from core.settings import BASE_DIR, STATIC_ROOT, STATICFILES_DIRS
import os

def cadastro(request): 
    print(os.path.join(BASE_DIR, 'templates'))
    print(STATICFILES_DIRS)
    pessoa = "Joao"
    return render(request, "cadastro\index.html", {"pessoas": pessoa}) 