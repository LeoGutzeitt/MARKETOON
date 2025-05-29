from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from loja import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro_produto, name='cadastro'),
    path('produto/<int:id>/', views.detalhes_produto, name='detalhes_produto'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/remover/<int:produto_id>/', views.remover_wishlist, name='remover_wishlist'),
    path('wishlist/adicionar/<int:produto_id>/', views.adicionar_wishlist, name='adicionar_wishlist'),
    path('wishlist/limpar/', views.limpar_wishlist, name='limpar_wishlist'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('adicionar-carrinho/<int:produto_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('remover-carrinho/<int:produto_id>/', views.remover_carrinho, name='remover_carrinho'),
    path('limpar-carrinho/', views.limpar_carrinho, name='limpar_carrinho'),
    path('produtos/', views.produtos, name='produtos'),
    path('compra/<int:produto_id>/', views.pagina_de_compra, name='pagina_de_compra'),
    path('suporte/', views.suporte, name='suporte'),
    path('pagamento/', views.pagina_pagamento, name='pagina_pagamento'),
    path('login/', views.login_view, name='login'),  # sua própria view
    path('logout/', views.logout_view, name='logout'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('processar_pagamento/', views.processar_pagamento, name='processar_pagamento'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
