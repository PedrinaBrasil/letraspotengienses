from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('Nome', max_length=100, blank=True, null=False)
    bio = models.TextField('Biografia', max_length=1000, blank=True)
   
    citation = models.CharField('Citação', max_length=100, blank=True, null= False)
    date_created = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    date_updated =models.DateTimeField('Atualizado em', auto_now=True) 
    
    REQUIRED_FIELDS = ['name', 'citation']


    class Gender(models.TextChoices):
        MALE = 'Masculino', _('Masculino')
        FEMALE = 'Feminino', _('Feminino')
        OTHER = 'Outro', _('Outro')
    
    gender = models.CharField('Sexo',
        max_length=10,
        choices=Gender.choices,
        default=Gender.MALE,    
        blank=False)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name:'Autor'
        verbose_name_plural:'Autores'
