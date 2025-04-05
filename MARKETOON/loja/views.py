from django.shortcuts import render,redirect
from loja.models import func_registrar_produto

# Create your views here.
def home(request):
    return render(request, 'loja/home.html')

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


