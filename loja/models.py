from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class func_registrar_produto(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='produtos/')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name="Data de criação")

    vendido = models.BooleanField(default=False)  # ← novo campo
    TIPO_DIREITO_CHOICES = [
        ('compartilhado', 'Direito Compartilhado'),
        ('pleno', 'Direito Pleno'),
    ]
    tipo_direito = models.CharField(
        max_length=20,
        choices=TIPO_DIREITO_CHOICES,
        default='compartilhado'
    )

    def __str__(self):
        return self.nome


class Wishlist(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(func_registrar_produto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} deseja {self.produto.nome}"
