from django.contrib import admin
from Cars.models import Cars
# Register your models here.

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ano', 'preco', 'marca', )
    search_fields = ('nome', )