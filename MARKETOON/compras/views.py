from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto

def pagina_inicial(request):
    produtos = Produto.objects.filter(comprado=False) 
    return render(request, 'pagina_inicial.html', {'produtos': produtos})

def comprar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if produto.nome == "Direto Pleno":  
        produto.comprado = True
        produto.save()

    return redirect('pagina_inicial')  
