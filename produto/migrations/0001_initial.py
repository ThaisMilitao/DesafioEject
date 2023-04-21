# Generated by Django 4.1.7 on 2023-04-11 00:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('email', models.EmailField(max_length=200, verbose_name='email')),
                ('preco', models.IntegerField()),
                ('imagem', models.ImageField(upload_to='fotos/%d/%m/%Y/')),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(choices=[('Eletrônicos', 'Eletrônicos'), ('Televisão', 'Televisão'), ('Computador', 'Computador'), ('Celular', 'Celular'), ('Áudio e Vídeo', 'Áudio e Vídeo')], default='Eletrônicos', max_length=50)),
                ('data', models.DateField(default=datetime.datetime.now)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario')),
            ],
        ),
    ]
