from django.shortcuts import render,redirect
from loja.models import func_registrar_produto
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


# Create your views here.
def detalhes_produto(request, id):
    produto = get_object_or_404(func_registrar_produto, id=id)
    return render(request, 'loja/detalhes_produto.html', {'produto': produto})


def home(request):
    query = request.GET.get('q', '')
    produtos = func_registrar_produto.objects.all()

    if query:
        produtos = produtos.filter(
            Q(nome__icontains=query) |
            Q(descricao__icontains=query)
        )

    paginator = Paginator(produtos, 12)  # ou a paginação que estiver usando
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

def adicionar_carrinho(request, produto_id):
    produto = get_object_or_404(func_registrar_produto, id=produto_id)
    carrinho = request.session.get('carrinho', [])
    if produto_id not in carrinho:
        carrinho.append(produto_id)
        request.session['carrinho'] = carrinho
    return redirect('wishlist') 