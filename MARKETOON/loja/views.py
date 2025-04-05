from django.shortcuts import render,redirect
from loja.models import func_registrar_produto
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404


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
        
        return redirect('pagina_inicial')

    return render(request, 'loja/html.html')




