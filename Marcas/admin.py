from django.contrib import admin
from Marcas.models import Marca
# Register your models here.

@admin.register(Marca)
class MarcasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', )
    search_fields = ('nome', )