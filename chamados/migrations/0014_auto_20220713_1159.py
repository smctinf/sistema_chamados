# Generated by Django 3.2.13 on 2022-07-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0013_auto_20220711_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tecnico',
            options={'ordering': ['user']},
        ),
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(blank=True, default='00000000000', max_length=11, null=True),
        ),
    ]
