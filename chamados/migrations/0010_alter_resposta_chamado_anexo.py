# Generated by Django 3.2.13 on 2022-07-11 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0009_auto_20220711_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resposta_chamado',
            name='anexo',
            field=models.FileField(blank=True, null=True, upload_to='anexos_chamados', verbose_name='Anexo'),
        ),
    ]
