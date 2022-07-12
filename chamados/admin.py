from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Tipo_Chamado)
admin.site.register(Tipo_Suporte)
admin.site.register(Chamado)
admin.site.register(Impressora)
admin.site.register(Chamado_Impressora)
admin.site.register(Resposta_chamado)
admin.site.register(Status)
admin.site.register(Tecnico)