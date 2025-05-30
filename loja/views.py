from loja.models import func_registrar_produto, Perfil
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your views here.
def detalhes_produto(request, id):
    produto = get_object_or_404(func_registrar_produto, id=id)
    return render(request, 'loja/detalhes_produto.html', {'produto': produto})


def home(request):
    query = request.GET.get('q', '')
    produtos = func_registrar_produto.objects.filter(vendido=False)

    if query:
        produtos = produtos.filter(
            Q(nome__icontains=query) |
            Q(descricao__icontains=query)
        )

    paginator = Paginator(produtos, 12)
    page = request.GET.get('page')
    produtos_paginados = paginator.get_page(page)

    return render(request, 'loja/home.html', {'produtos': produtos_paginados})


def cadastro_produto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco")
        imagem = request.FILES.get("imagem")
        
        func_registrar_produto.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            descricao=descricao,
            preco=preco,
            imagem=imagem
        )
        
        return redirect('/')

    return render(request, 'loja/html.html')



def wishlist_view(request):
    wishlist_ids = request.session.get('wishlist', [])
    produtos = func_registrar_produto.objects.filter(id__in=wishlist_ids)
    return render(request, 'loja/wishlist.html', {'wishlist': produtos})


def adicionar_wishlist(request, produto_id):
    produto = get_object_or_404(func_registrar_produto, id=produto_id)
    wishlist = request.session.get('wishlist', [])

    if produto_id not in wishlist:
        wishlist.append(produto_id)
        request.session['wishlist'] = wishlist

    return redirect('wishlist')


def remover_wishlist(request, produto_id):
    wishlist = request.session.get('wishlist', [])

    if produto_id in wishlist:
        wishlist.remove(produto_id)
        request.session['wishlist'] = wishlist

    return redirect('wishlist')


def limpar_wishlist(request):
    if request.method == 'POST':
        request.session['wishlist'] = []
    return redirect('wishlist')

def checkout_view(request):
    return render(request, 'loja/checkout.html')

def carrinho(request):
    carrinho_ids = request.session.get('carrinho', [])
    produtos = func_registrar_produto.objects.filter(id__in=carrinho_ids)
    if not produtos:
        return render(request, 'loja/carrinho.html', {'produtos': produtos, 'mensagem': 'Seu carrinho está vazio.'})

    return render(request, 'loja/carrinho.html', {'produtos': produtos})

def adicionar_carrinho(request, produto_id):
    produto = get_object_or_404(func_registrar_produto, id=produto_id)
    carrinho = request.session.get('carrinho', [])
    if produto_id not in carrinho:
        carrinho.append(produto_id)
        request.session['carrinho'] = carrinho
    return redirect('carrinho')

def remover_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', [])
    if produto_id in carrinho:
        carrinho.remove(produto_id)
        request.session['carrinho'] = carrinho
    return redirect('carrinho')

def limpar_carrinho(request):
    if request.method == 'POST':
        request.session['carrinho'] = []
    return redirect('carrinho') 

def produtos(request):
    produtos = func_registrar_produto.objects.all()  
    return render(request, 'loja/produtos.html', {'produtos': produtos})


def pagina_de_compra(request, produto_id):
    produto = get_object_or_404(func_registrar_produto, id=produto_id)
    contexto = {
        'produto': {
            'id': produto.id,
            'nome': produto.nome,
            'preco_basico': produto.preco,
            'preco_pleno': produto.preco,
            'descricao': produto.descricao,
            'email': produto.email,
            'telefone': produto.telefone,
        }
    }
    return render(request, 'loja/pag-de-compra.html', contexto)

  

def suporte(request):
    return render(request, 'loja/suporte.html')

def pagina_pagamento(request):
    produto_id = request.GET.get('produto_id')
    plano = request.GET.get('plano')

    produto = get_object_or_404(func_registrar_produto, id=produto_id)

    contexto = {
        'produto': produto,
        'plano': plano,
    }
    return render(request, 'loja/pagamento.html', contexto)
    

def processar_pagamento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cartao = request.POST.get('cartao')
        validade = request.POST.get('validade')
        cvv = request.POST.get('cvv')
        produto_id = request.POST.get('produto_id')
        plano = request.POST.get('plano')

        try:
            produto = func_registrar_produto.objects.get(id=produto_id)
        except func_registrar_produto.DoesNotExist:
            return HttpResponse("Produto não encontrado", status=404)
        
        if plano == 'pleno':
            produto.vendido = True
            produto.tipo_direito = 'pleno'
            produto.save()
        

        return redirect('home')
    return redirect('checkout') 




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            # Garante que o perfil existe
            Perfil.objects.get_or_create(usuario=user)

            return redirect('home')  
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'loja/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')


from django.contrib.auth.models import User

def cadastrar(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
        else:
            User.objects.create_user(username=username, password=password1, email=email)
            messages.success(request, 'Conta criada com sucesso. Faça login.')
            return redirect('login')  # certifique-se de ter uma URL chamada 'login'

    return render(request, 'loja/cadastro.html')


@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)


from .models import Produto 
from django.contrib import messages

def perfil(request):
    user = request.user
    perfil, created = Perfil.objects.get_or_create(user=user)

    if request.method == 'POST':
        user.first_name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.save()

        if 'imagem' in request.FILES:
            perfil.imagem = request.FILES['imagem']

        
        
        perfil.descricao = request.POST.get('descricao')
        perfil.is_vendedor = 'vendedor' in request.POST

        produtos_ids = request.POST.getlist('produtos')
        perfil.produtos.set(produtos_ids)

        perfil.save()
        messages.success(request, "Perfil atualizado com sucesso.")

        return redirect('perfil')

    produtos_disponiveis = Produto.objects.all()

    return render(request, 'loja/perfil.html', {
    'user': user,
    'perfil': perfil,
    'produtos_disponiveis': produtos_disponiveis,
})