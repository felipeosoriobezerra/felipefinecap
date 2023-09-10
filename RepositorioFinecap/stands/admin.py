from django.contrib import admin
from .models import *

@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display=('localizacao','valor',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display=('nome_empresa','cnpj','quitado','categoria_empresa',)