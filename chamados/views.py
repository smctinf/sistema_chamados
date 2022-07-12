from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, update_session_auth_hash

from chamados.models import Status, Tecnico

from .forms import *

@login_required
def index(request):
    chamados_abertos=Chamado.objects.filter(ativo=True)
    chamados_fechados=Chamado.objects.filter(ativo=False)
    context={
        'meus_chamados': Chamado.objects.filter(create_user=request.user, ativo=True),
        'chamados_fechados': chamados_fechados.count(),
        'chamados_abertos': chamados_abertos.count(),
    }    
    if not request.user.is_staff:
        usuario=Usuario.objects.get(user=request.user)    
        error=''
        save=False
        if request.method=='POST':
            form=Form_Chamado(request.POST, request.FILES)
            if form.is_valid():            
                if request.POST['tipo_chamado']=='1':
                    form_imp=Form_Chamado_Impressora(request.POST)
                    if form_imp.is_valid():
                        chamado=form.save()
                        chamado.status=Status.objects.get(id='1')
                        chamado.create_user=request.user
                        chamado.save()
                        chamado_imp=form_imp.save()
                        chamado_imp.chamado=chamado                    
                        chamado_imp.save()
                        save=True
                    else:
                        print('error: impressora')
                else:
                    chamado=form.save()
                    chamado.create_user=request.user
                    chamado.save()
            else:
                error=form.errors
                print('error: form')   
        form=Form_Chamado()         
        context={
            'usuario': usuario,
            'form': form,
            'error': error,
            'save': save,
            'meus_chamados': Chamado.objects.filter(create_user=request.user, ativo=True),
            'chamados_fechados': chamados_fechados.count(),
            'chamados_abertos': chamados_abertos.count(),
        }
    return render(request, 'chamados/index.html', context)

@login_required
def listar_chamados(request):
    context={    
        'meus_chamados': Chamado.objects.filter(create_user=request.user, ativo=True)
    }
    if request.user.is_staff:
        if request.user.is_superuser:
            chamados=Chamado.objects.all()
        else:
            chamados=Chamado.objects.filter(ativo=True, tecnico=Tecnico.objects.get(user=request.user.id))
        
        context={
            'chamados': chamados,
            'meus_chamados': Chamado.objects.filter(create_user=request.user, ativo=True)
        }

    return render(request, 'chamados/listar_chamados.html', context)
    
@login_required
def editar_chamado(request, id):
    chamado=Chamado.objects.get(id=id)
    usuario=Usuario.objects.get(id=chamado.create_user.id)
    form=Form_Chamado_Edit(instance=chamado)
    if request.method=='POST':
        form=Form_Chamado_Edit(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    context={
        'chamado': chamado,
        'usuario': usuario,
        'form': form,          
        'meus_chamados': Chamado.objects.filter(create_user=request.user, ativo=True)      
    }
    return render(request, 'chamados/editar_chamado.html', context)

@login_required
def detalhes_chamado(request, id):
    chamado=Chamado.objects.get(id=id)
    usuario=Usuario.objects.get(id=chamado.create_user.id)
    form=Form_Resposta()
    historico=Resposta_chamado.objects.filter(chamado=chamado)
    if request.method=='POST':
        form=Form_Resposta(request.POST, request.FILES)
        if form.is_valid():
            resposta=form.save()
            if len(request.FILES)>0:
                resposta.tem_anexo=True
            resposta.chamado=chamado
            resposta.user=request.user
            resposta.save()
        else:
            print(form.errors)
    context={
        'chamado': chamado,
        'usuario': usuario,
        'form': form,
        'historico_status': len(historico)>0,
        'historico': historico,
        'meus_chamados': Chamado.objects.filter(create_user=request.user, ativo=True)
    }
    return render(request, 'chamados/detalhes_chamados.html', context)
     

@login_required
def novo_chamado(request):
    usuario=Usuario.objects.get(user=request.user)    
    error=''
    save=False
    if request.method=='POST':

        form=Form_Chamado(request.POST, request.FILES)
        if form.is_valid():            
            if request.POST['tipo_chamado']=='1':
                form_imp=Form_Chamado_Impressora(request.POST)
                if form_imp.is_valid():
                    chamado=form.save()
                    chamado.status=Status.objects.get(id='1')
                    chamado.create_user=request.user
                    if len(request.FILES)>0:
                        chamado.tem_anexo=True
                    chamado.save()
                    chamado_imp=form_imp.save()
                    chamado_imp.chamado=chamado                    
                    chamado_imp.save()
                    save=True
                else:
                    print('error: impressora')
            else:
                chamado=form.save()
                chamado.create_user=request.user
                chamado.save()
        else:
            error=form.errors
            print('error: form')   
    form=Form_Chamado()         
    context={
        'usuario': usuario,
        'form': form,
        'error': error,
        'save': save,
        'meus_chamados': Chamado.objects.filter(create_user=request.user, ativo=True)
    }
    return render(request, 'chamados/novo_chamado.html', context)

@login_required
def get_tipo_suporte(request):
    tipo_chamado=Tipo_Chamado.objects.get(id=request.GET.get('id'))
    tipo=Tipo_Suporte.objects.filter(tipo_chamado=tipo_chamado)
    print(tipo)
    context={
        'tipo': tipo
    }
    return render(request, 'chamados/get/tipo_suporte.html', context)

@login_required
def get_chamado_impressora(request):
    context={
        'form': Form_Chamado_Impressora()
    }
    return render(request, 'chamados/get/chamado_impressora.html', context)

def cadastrar(request):
    forms=Form_User()
    forms_usuario=Form_Usuario()
    if request.method=='POST':
        forms=Form_User(request.POST)
        forms_usuario=Form_Usuario(request.POST)
        if forms.is_valid() and forms_usuario.is_valid():
            user=forms.save()
            user.set_password(user.password)
            user.save()
            usuario=forms_usuario.save()
            usuario.user=user
            usuario.save()
            return redirect('login')
        else:
            print(forms.errors)
            print(forms_usuario.errors)
    context={
        'forms': forms,
        'forms_usuario': forms_usuario
    }
    return render(request, 'registration/signup.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':               
        username = request.POST['username']
        password = request.POST['password']        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:                
            context={
                'error': True,                
            }
            return render(request, 'registration/login.html', context)
    else:
        context={
            'error2': True,                    
        }
        return render(request, 'registration/login.html', context)    