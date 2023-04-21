from django.db import models
from datetime import datetime
from usuario.models import Usuario
import string
import random
# Create your models here.

def gerarCodigo(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

class Produtos(models.Model):
    nome = models.CharField(verbose_name='nome', max_length=200)
    email = models.EmailField(verbose_name='email', max_length=200)
    preco = models.IntegerField()
    imagem = models.ImageField(upload_to='fotos/%d/%m/%Y/')
    descricao =models.TextField()
    codigo = models.CharField(default=gerarCodigo(), max_length=6)

    CATEGORIA_CHOICES = (
    ("Eletrônicos", "Eletrônicos"),
    ("Televisão", "Televisão"),
    ("Computador", "Computador"),
    ("Celular", "Celular"),
    ("Áudio e Vídeo", "Áudio e Vídeo"),
    )

    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default="Eletrônicos")
    data = models.DateField(default=datetime.now())

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    
