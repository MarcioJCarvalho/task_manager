from os import name
import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True, verbose_name="Nome")

    def __str__(self) -> str:
        return "{}".format(self.name)
    
class Comment(models.Model):
    # TODO incluir chaves estrangeiras
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(verbose_name="Comentários")
    creation_date = models.DateField(verbose_name="Criação")    

    def __str__(self) -> str:
        return "{}".format(self.text)
    
class Auditable(models.Model):
    # mudar para histórico
    # data e hora
    # TODO incluir chaves estrangeiras
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    action = models.TextField(verbose_name="Ação")
    timestamp = models.DateField(verbose_name="Data") 

    def __str__(self) -> str:
        return "{}".format(self.action)
    
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, unique=True, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    due_date = models.DateField(verbose_name="Prazo")
    creation_date = models.DateField(verbose_name="Criação")
    completion_date = models.DateField(null=True, blank=True, verbose_name="Finalização")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='pdf/', null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="tasks_as_usuario") 


    def __str__(self) -> str:
        return "{}".format(self.title)