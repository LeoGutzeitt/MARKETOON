"""
URL configuration for MARKETOON project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from loja.views import cadastro_produto,home
from django.conf import settings
from django.conf.urls.static import static
from loja import views
from loja.views import wishlist_view, remover_wishlist, adicionar_wishlist, limpar_wishlist, checkout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/',cadastro_produto, name='cadastro'),
    path('', home, name='home'),
    path('produto/<int:id>/', views.detalhes_produto, name='detalhes_produto'),
    path('wishlist/', wishlist_view, name='wishlist'),
    path('wishlist/remover/<int:produto_id>/', remover_wishlist, name='remover_wishlist'),
    path('wishlist/adicionar/<int:produto_id>/', adicionar_wishlist, name='adicionar_wishlist'),
    path('wishlist/limpar/', limpar_wishlist, name='limpar_wishlist'),
    path('checkout/', checkout_view, name='checkout'),  
    path('wishlist/adicionar/<int:produto_id>/', views.adicionar_wishlist, name='adicionar_wishlist'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)