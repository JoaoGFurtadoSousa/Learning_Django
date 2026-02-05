from django.urls import path
from . import views


urlpatterns = [
    path('teste/', views.cadastro),
    path('cadastro/', views.salvar_pessoa_no_banco, name= 'salva_pessoa'),
    path('listar_pessoas/', views.lista_todas_as_pessoas),
    path('login/', views.login, name="login"),
    ]