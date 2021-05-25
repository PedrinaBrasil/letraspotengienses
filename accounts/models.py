import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('E-mail', unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'O e-mail não pode conter espaços', 'invalid')])
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É administrador?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    date_updated =models.DateTimeField('Atualizado em', auto_now=True) 
    
    class Occupation(models.TextChoices):
        STUDENT = 'Estudante', _('Estudante')
        PROFESSIONAL = 'Profissional', _('Profissional')
        OTHER = 'Outro', _('Outro')
    
    ocucupation = models.CharField('Ocupação',
        max_length=12,
        choices=Occupation.choices,
        default=Occupation.STUDENT,    
        blank=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'ocucupation']

    def __str__(self):
        return self.name or self.email
    
    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name:'Usuário'
        verbose_name_plural:'Usuários'

class PasswordReset(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete=models.PROTECT, related_name='resets')
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)

    class Meta:
        verbose_name='Nova Senha'
        verbose_name_plural='Novas Senhas'
        ordering = ['-created_at']
