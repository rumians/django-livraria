# Generated by Django 5.1.7 on 2025-04-07 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_descricao_editora_nome_editora_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
