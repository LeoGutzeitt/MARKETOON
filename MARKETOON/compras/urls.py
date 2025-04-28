
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('comprar/<int:produto_id>/', views.comprar_produto, name='comprar_produto'),
]
