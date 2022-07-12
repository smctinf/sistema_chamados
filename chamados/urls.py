from tabnanny import verbose
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    
    path('get_tipo_suporte/', views.get_tipo_suporte),
    path('get_chamado_impressora/', views.get_chamado_impressora),
    
    path('novo-chamado/', views.novo_chamado, name='novo_chamado'),
    path('listar-chamados/', views.listar_chamados, name='listar_chamados'),    
    path('detalhe-chamado/<id>', views.detalhes_chamado, name='detalhe_chamado'),
    path('detalhe-chamado/<id>/editar', views.editar_chamado, name='editar_chamado'),
    
    path('login/', views.login_view, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]
