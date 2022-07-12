from django import forms
from django.forms import ModelForm, ValidationError

from django.contrib.auth.models import User
from .models import Usuario, Tipo_Chamado, Tipo_Suporte, Chamado, Impressora, Chamado_Impressora, Resposta_chamado

class Form_User(ModelForm):
    class Meta:
        model = User    
        widgets = {            
          'username': forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off'}),
          'password': forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off', 'type': 'password'}),
          'first_name': forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off', 'required': 'true'}),
        } 
        exclude = ['last_login', 'is_superuser', 'groups', 'user_permissions',
        'last_name',  'email', 'is_staff', 'is_active', 'date_joined']

                # <div class="form-floating mb-3">
                #     <input type="email" class="form-control" id="floatingInput" name="username" placeholder="name@example.com">
                #     <label for="floatingInput">Email</label>
                # </div>
                # <div class="form-floating mb-4">
                #     <input type="password" class="form-control" id="floatingPassword" name="password" placeholder="Password">
                #     <label for="floatingPassword">Senha</label>
                # </div>
class Form_Usuario(ModelForm):
    class Meta:
        model = Usuario
        widgets = {            
          'secretaria': forms.Textarea(attrs={'rows':1, 'class': 'form-control'}),
          'setor': forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off'}),
          'matricula': forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off'}),
          'telefone': forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off'}),
          'ramal': forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off'}),
        } 
        exclude = ['user', 'dt_inclusao']

class Form_Tipo_Chamado(ModelForm):
    class Meta:
        model = Tipo_Chamado
        exclude = ['create_user', 'dt_inclusao']

class Form_Tipo_Suporte(ModelForm):
    class Meta:
        model = Tipo_Suporte
        exclude = ['create_user', 'dt_inclusao']

class Form_Chamado(ModelForm):
    class Meta:
        model = Chamado
        widgets={
            'tipo_chamado': forms.Select(attrs={'class':'form-control', 'onchange': 'get_tipo_suporte(this.value)'}),
            'tipo_suporte': forms.Select(attrs={'class':'form-control'}),
            'mensagem': forms.Textarea(attrs={'class':'form-control'}),
        }
        exclude = ['ativo',     'tem_anexo', 'status', 'create_user', 'dt_inclusao']

class Form_Chamado_Edit(ModelForm):
    class Meta:
        model = Chamado
        widgets={
            'tipo_chamado': forms.Select(attrs={'class':'form-control', 'onchange': 'get_tipo_suporte(this.value)'}),
            'tipo_suporte': forms.Select(attrs={'class':'form-control'}),
            'mensagem': forms.Textarea(attrs={'class':'form-control mb-3'}),
            'status': forms.Select(attrs={'class':'form-control mb-3'}),
            'tecnico': forms.Select(attrs={'class':'form-control mb-3'})
        }
        exclude = ['ativo', 'tem_anexo', 'tipo_chamado', 'tipo_suporte','anexo', 'create_user', 'dt_inclusao']


class Form_Impressora(ModelForm):
    class Meta:
        model = Impressora
        exclude = ['create_user', 'dt_inclusao']

class Form_Chamado_Impressora(ModelForm):
    class Meta:
        model = Chamado_Impressora
        widgets={
            'impressora': forms.Select(attrs={'class':'form-control'}),
            'n_serie': forms.TextInput(attrs={'class':'form-control'}),
            'contador': forms.TextInput(attrs={'class':'form-control'}),
        }
        exclude = ['chamado','create_user', 'dt_inclusao']

class Form_Resposta(ModelForm):
    class Meta:
        model = Resposta_chamado
        widgets={
            'resposta': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
        }
        exclude = ['tem_anexo', 'user', 'dt_inclusao']
