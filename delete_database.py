import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MARKETOON.settings')
django.setup()

from loja.models import func_registrar_produto
from loja.models import Wishlist



func_registrar_produto.objects.all().delete()
Wishlist.objects.all().delete()
print("Todos os dados foram deletados.")