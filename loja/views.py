from django.shortcuts import render, redirect
from loja.models import Produto, Pedido
from loja.forms import ProdutoForm, PedidoForm


def home(request):
    return render(request, 'loja/index.html')


def createProduto(request):
    form = ProdutoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('readProduto')
    
    data = {}
    data['form'] = form
    return render(request, 'loja/produto/createProduto.html', data)

def readProduto(request):
    data = {}
    data['produtos'] = Produto.objects.all()
    return render(request, 'loja/produto/readProduto.html', data)

def updateProduto(request, pk):
    produto = Produto.objects.get(id=pk)
    form = ProdutoForm(request.POST or None, instance=produto)
    
    if form.is_valid():
        form.save()
        return redirect('readProduto')
    
    data = {'form': form, 'produto': produto}
    data['form'] = form
    return render(request, 'loja/produto/updateProduto.html', data)

def deleteProduto(request, pk):
    produto = Produto.objects.get(id=pk)
    produto.delete()
    return redirect('readProduto')


def createPedido(request):
    form = PedidoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('readPedido')
    
    data = {}
    data['form'] = form
    return render(request, 'loja/pedido/createPedido.html', data)

def readPedido(request):
    data = {}
    data['pedidos'] = Pedido.objects.all()
    return render(request, 'loja/pedido/readPedido.html', data)

def updatePedido(request, pk):
    pedido = Pedido.objects.get(id=pk)
    form = PedidoForm(request.POST or None, instance=pedido)
    
    if form.is_valid():
        form.save()
        return redirect('readProduto')
    
    data = {'form': form, 'pedido': pedido}
    data['form'] = form
    return render(request, 'loja/pedido/updatePedido.html', data)

def deletePedido(request, pk):
    pedido = Pedido.objects.get(id=pk)
    pedido.delete()
    return redirect('readPedido')