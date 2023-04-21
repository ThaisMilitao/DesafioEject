from atexit import register
from xml.dom import ValidationErr
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import re

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user=user) 
            if remember is None:
                request.session.set_expiry(0)
            
            return redirect('dashboard')
        messages.error(request, 'Username e/ou senha inválido.')  
    return render(request, 'index.html')
    
@login_required(login_url='login')
def logout(request): 
    auth.logout(request)
    return redirect('login')

def signin(request):
    if request.method == "GET":
        return render(request, 'auth-register.html')
    else:
        email = request.POST.get('email')
        name = request.POST.get('fullName')
        username = request.POST.get('username') 
        password = request.POST.get('password')
        password2 = request.POST.get('password2') 
        
        if not Usuario.objects.filter(user__username=username).exists():
            if validarSenha(password):
                messages.error(request, 'Requisitos:\n*Minimo 8 caracteres\n*Pelo menos 2 letras minuscula\n*Pelo menos 2 letras Maiuscula\n*Pelo menos 2 numeros\n*Pelo menos 1 caractere especial')
                return render(request, 'auth-register.html')
            if (password and password2) and password != password2:
                messages.error(request, 'As senhas digitadas não coincidem')
                return render(request, 'auth-register.html')
        
            else:
                user = User.objects.create_user(email=email, first_name = name, username=username, password=password)
                user.save()
                Usuario(user=user).save()

        return redirect('login')

@login_required(login_url='login')
def editar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    user = User.objects.get(id=id)
    
    context ={
        'user': usuario,
    }

    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('fullName')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')                
        imagem= request.FILES.get('imagem')

        usuario.imagem = imagem
        user.email = email
        user.first_name = name
        user.set_password(password)
        
        if validarSenha(password):
            messages.error(request, 'Requisitos:\n*Minimo 8 caracteres\n*Pelo menos 2 letras minuscula\n*Pelo menos 2 letras Maiuscula\n*Pelo menos 2 numeros\n*Pelo menos 1 caractere especial')
            return render(request, 'editar-usuario.html', context)
            
        if (password and password2) and password != password2:
            messages.error(request, 'As senhas digitadas não coincidem')
            return render(request, 'editar-usuario.html', context)
        
        else: 
            user.save()
            usuario.save()
            messages.success(request, 'Dados alterados com sucesso!')


    
    return render(request, 'editar-usuario.html', context)

def validarSenha(password):
    min_numero = 2
    min_letraMaiuscula = 2
    min_letraMinuscula = 2
    min_carac_especial = 1
    tamanho_minimo = 8
    
    if len(password or ()) < tamanho_minimo:
        return ValidationErr("Tamanho minimo de" + str(tamanho_minimo) + "caracteres")
    if len(re.findall(r"[A-Z]", password)) < min_letraMaiuscula:
        return ValidationErr("Possuir pelo menos" + str(min_letraMaiuscula) + "letra Maiuscula")
    if len(re.findall(r"[a-z]", password)) < min_letraMinuscula:
        return ValidationErr("Possuir pelo menos" + str(min_letraMinuscula) + "letra minuscula")
    if len(re.findall(r"[0-9]", password)) < min_numero:
        return ValidationErr("Possuir pelo menos" + str(min_numero) + "numeros")
    if len(re.findall(r"[!#$%&'*+-.^_`|~:]", password)) < min_carac_especial:
        return ValidationErr("Possuir pelo menos" + str(min_carac_especial) + "caractere especial")
