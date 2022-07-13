from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    cpf=models.CharField(max_length=11, null=True, blank=True, default='00000000000')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    secretaria=models.TextField(verbose_name='Nome da secretaria', blank=False)
    setor=models.CharField(max_length=150, verbose_name='Subsecretaria/Setor', blank=False)
    matricula=models.CharField(max_length=8, verbose_name='Matricula')
    telefone=models.CharField(max_length=11, blank=False)
    ramal=models.CharField(max_length=5)                        
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')
    # dt_alteracao = models.DateTimeField(auto_now=True, verbose_name='Dt. Alteração')
    
    def __str__(self):
        return '%s' % (self.user)

class Tecnico(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    # dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')
    #dt_alteracao = models.DateTimeField(auto_now=True, verbose_name='Dt. Alteração')

    class Meta:    
        ordering = ['user']
    def __str__(self):
        return '%s' % (self.user.first_name)

class Tipo_Chamado(models.Model):
    
    class Meta:    
        ordering = ['tipo']

    tipo=models.CharField(max_length=80, verbose_name='Tipo de chamado', blank=False)
    create_user=models.ForeignKey(Usuario, on_delete=models.PROTECT, default=1)
    # user=models.ForeignKey(Usuario, on_delete=models.CASCADE)                    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')
    #dt_alteracao = models.DateTimeField(auto_now=True, verbose_name='Dt. Alteração')

    def __str__(self):
        return '%s' % (self.tipo)

class Tipo_Suporte(models.Model):
    tipo_chamado=models.ForeignKey(Tipo_Chamado, on_delete=models.PROTECT, blank=False)
    tipo=models.CharField(max_length=80, verbose_name='Tipo de suporte', blank=False)
    create_user=models.ForeignKey(User, on_delete=models.PROTECT)                    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')
    #dt_alteracao = models.DateTimeField(auto_now=True, verbose_name='Dt. Alteração')

    def __str__(self):
        return '%s - %s' % (self.tipo_chamado,self.tipo)

class Status(models.Model):
    name=models.CharField(max_length=85, blank=False)
    bg=models.CharField(max_length=85, blank=False, default='')

    def __str__(self):
        return '%s' % (self.name)

class Chamado(models.Model):
    ativo=models.BooleanField(default=True)
    tipo_chamado=models.ForeignKey(Tipo_Chamado, on_delete=models.PROTECT, verbose_name='Tipo de chamado', blank=False)
    tipo_suporte=models.ForeignKey(Tipo_Suporte, on_delete=models.PROTECT, verbose_name='Tipo de suporte', blank=False)
    mensagem=models.TextField(blank=False)    
    anexo=models.FileField(upload_to='anexos_chamados', verbose_name='Anexo', default=None, null=True, blank=True)    
    tem_anexo=models.BooleanField(default=False)
    status=models.ForeignKey(Status, on_delete=models.PROTECT, blank=True, null=True)
    tecnico=models.ForeignKey(Tecnico, on_delete=models.PROTECT, blank=True, null=True)
    create_user=models.ForeignKey(User, on_delete=models.PROTECT, null=True)                    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')
    #dt_alteracao = models.DateTimeField(auto_now=True, verbose_name='Dt. Alteração')

    def __str__(self):
        return '%s. %s - %s' % (self.id, self.tipo_chamado, self.tipo_suporte.tipo)

class Impressora(models.Model):
    modelo=models.CharField(max_length=50, blank=False)
    create_user=models.ForeignKey(User, on_delete=models.PROTECT, null=True)                    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')
    #dt_alteracao = models.DateTimeField(auto_now=True, verbose_name='Dt. Alteração')

    def __str__(self):
        return '%s' % (self.modelo)
        
class Chamado_Impressora(models.Model):
    chamado=models.ForeignKey(Chamado, on_delete=models.CASCADE, blank=True, null=True)
    impressora=models.ForeignKey(Impressora, on_delete=models.PROTECT, blank=False, verbose_name='Modelo da impressora')
    n_serie=models.CharField(max_length=15, blank=False, verbose_name='Número de serie')
    contador=models.IntegerField(blank=False)   
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')
    #dt_alteracao = models.DateTimeField(auto_now=True, verbose_name='Dt. Alteração')

class Resposta_chamado(models.Model):
    chamado=models.ForeignKey(Chamado, on_delete=models.CASCADE, blank=True ,null=True)
    resposta=models.TextField()
    anexo=models.FileField(upload_to='anexos_chamados', verbose_name='Anexo', default=None, null=True, blank=True)    
    tem_anexo=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.PROTECT, null=True)                    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')
    #dt_alteracao = models.DateTimeField(auto_now=True, verbose_name='Dt. Alteração')