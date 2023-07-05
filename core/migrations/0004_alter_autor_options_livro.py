# Generated by Django 4.2 on 2023-04-05 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_autor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autores'},
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('titulo', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=32)),
                ('quantidade', models.IntegerField()),
                ('preco', models.FloatField()),
                (
                    'categoria',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='livros',
                        to='core.categoria',
                    ),
                ),
                (
                    'editora',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='livros',
                        to='core.editora',
                    ),
                ),
            ],
        ),
    ]
