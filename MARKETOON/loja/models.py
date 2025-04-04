from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class func_registrar_produto(models.Model):
    nome=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    telefone=models.CharField(max_length=11)
    preco=models.CharField(max_length=100)
    descricao= models.TextField(blank=True,null=True)
    data_criacao=models.DateTimeField(auto_now=True,verbose_name="Data de criação")
