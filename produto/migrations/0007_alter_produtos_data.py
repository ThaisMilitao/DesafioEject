# Generated by Django 4.1.7 on 2023-04-18 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_alter_produtos_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='data',
            field=models.DateField(default='04/18/23'),
        ),
    ]
