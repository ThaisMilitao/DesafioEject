from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Produtos
from usuario.models import Usuario
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    produtos = Produtos.objects.all().order_by('-data')
    tamanho = Produtos.objects.all().count
    ultimoPost = Produtos.objects.last

    if 'search' in request.GET:
        buscar = request.GET['search'] 
        produtos = Produtos.objects.filter(nome__contains=buscar).order_by('-data')

    page = request.GET.get('page', 1)
    paginator = Paginator(produtos, 3)

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    context = {
            'produtos': result,
            'tamanho': tamanho,
            'ultimoPost': ultimoPost,
            'p':produtos,

    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def meus_produtos(request):
    produtos = Produtos.objects.filter(usuario = Usuario.objects.get(user__username = request.user)).order_by('-data')
    
    if 'search' in request.GET:
        search = request.GET.get('search')
        produtos = Produtos.objects.filter(usuario = Usuario.objects.get(user__username = request.user)).filter(nome__contains=search).order_by('-data')



    page = request.GET.get('page', 1)
    paginator = Paginator(produtos, 3)

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    context = {
            'produtos': result,
            'p':produtos,
        }
    return render(request, 'meus-produtos.html', context)

@login_required(login_url='login')
def registrar_produtos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        preco= request.POST.get('preco')
        imagem= request.FILES.get('imagem')
        descricao= request.POST.get('descricao')
        categoria= request.POST.get('categoria')

        produto = Produtos(
            nome=nome,
            email=email,
            preco=preco,
            imagem=imagem,
            descricao=descricao,
            categoria=categoria,
            usuario = Usuario.objects.get(user__username = request.user)

        )
        produto.save()
        messages.success(request, 'Produto registrado com sucesso!')

    return render(request, 'registrar-produtos.html')

@login_required(login_url='login')
def editar_produto(request, id):
    produto = Produtos.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        preco= request.POST.get('preco')
        imagem= request.FILES.get('imagem')
        descricao= request.POST.get('descricao')
        categoria= request.POST.get('categoria')

        produto.nome = nome
        produto.email = email
        produto.preco =  preco
        produto.imagem = imagem
        produto.descricao = descricao
        produto.categoria= categoria
        produto.save()
        
        messages.success(request, 'Produto editado com sucesso!')
        return redirect ('meus-produtos')
    context = {
        'produto': produto,
    }
    return render(request, 'editar-produto.html', context)

@login_required(login_url='login')
def deletar_produto(request, id):
    produto = Produtos.objects.get(id=id)
    produto.delete()
    messages.success(request, 'Produto deletado com sucesso!')
    return redirect ('meus-produtos')