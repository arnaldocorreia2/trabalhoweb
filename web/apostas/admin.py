from django.contrib import admin
from .models import Jogador
from .models import Time
from .forms import JogadorForm
from .models import Partida
from  .models import Resultado
from django.contrib.auth.admin import UserAdmin
class UserAdmin(admin.ModelAdmin):
    form = JogadorForm

admin.site.register(Jogador,UserAdmin)
admin.site.register(Time)
admin.site.register(Partida)
admin.site.register(Resultado)