# Generated by Django 4.1.7 on 2023-04-17 23:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_produtos_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='data',
            field=models.DateField(default=datetime.datetime(2023, 4, 17, 20, 50, 19, 934352)),
        ),
    ]
