from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class func_registrar_produto(models.Model):
    nome=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    telefone=models.CharField(max_length=11)
    preco=models.DecimalField(max_digits=10,decimal_places=2)
    descricao= models.TextField(blank=True,null=True)
    imagem = models.ImageField(upload_to='produtos/')
    data_criacao=models.DateTimeField(auto_now=True,verbose_name="Data de criação")
