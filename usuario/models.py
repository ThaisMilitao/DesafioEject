from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    imagem = models.ImageField(null=True, blank=True, upload_to='usuario', default='usuario/user.png')
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        
    )
