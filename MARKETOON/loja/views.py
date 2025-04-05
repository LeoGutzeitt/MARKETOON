from django.shortcuts import render,redirect
from loja.models import func_registrar_produto
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def detalhes_produto(request, id):
    produto = get_object_or_404(func_registrar_produto, id=id)
    return render(request, 'loja/detalhes_produto.html', {'produto': produto})


def home(request):
    lista_produtos = func_registrar_produto.objects.all()
    paginator = Paginator(lista_produtos, 12)
    pagina = request.GET.get('page')
    produtos = paginator.get_page(pagina)
    return render(request, 'loja/home.html',{'produtos': produtos})

def cadastro_produto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco")
        imagem = request.FILES.get("imagem")
        func_registrar_produto.objects.create(nome=nome,
                                              email=email,
                                              telefone=telefone,
                                              descricao=descricao,
                                              preco=preco,
                                              imagem=imagem
                                              )
        
        return redirect('/')

    return render(request, 'loja/html.html')




def home(request):
    produtos = func_registrar_produto.objects.all()
    return render(request, 'loja/home.html', {'produtos': produtos})

# Cadastro de produto (POST)
def cadastro_produto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco")
        data = request.POST.get("data")
        func_registrar_produto.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            descricao=descricao,
            preco=preco,
            data=data
        )
        return redirect('home')
    return render(request, 'loja/cadastro.html')

# Página de detalhes do produto
def detalhes_produto(request, id):
    produto = get_object_or_404(func_registrar_produto, id=id)
    return render(request, 'loja/detalhes_produto.html', {'produto': produto})


##---------------------------------------whishlist

# Página da wishlist (sem usuário)
def wishlist_view(request):
    itens = Wishlist.objects.all()
    produtos = [item.produto for item in itens]
    return render(request, 'loja/wishlist.html', {'wishlist': produtos})

@csrf_exempt
def adicionar_wishlist(request, produto_id):
    produto = get_object_or_404(func_registrar_produto, id=produto_id)
    Wishlist.objects.get_or_create(produto=produto)
    return redirect('wishlist')

@csrf_exempt
def remover_wishlist(request, produto_id):
    produto = get_object_or_404(func_registrar_produto, id=produto_id)
    Wishlist.objects.filter(produto=produto).delete()
    return redirect('wishlist')

@csrf_exempt
def limpar_wishlist(request):
    if request.method == 'POST':
        Wishlist.objects.all().delete()
    return redirect('wishlist')

def checkout_view(request):
    return render(request, 'loja/checkout.html')

