# Generated by Django 3.0.7 on 2020-09-24 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(help_text='Descripcion de la categoria', max_length=60)),
                ('autor', models.ForeignKey(help_text='Seleccione el autor de la categoria', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(help_text='Escribe el titulo de la publicacion', max_length=200)),
                ('contenido', models.TextField(help_text='Escriba el contenido de la publicacion', max_length=2000)),
                ('f_pub', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Publicacion')),
                ('autor', models.ForeignKey(help_text='Seleccione el autor de la categoria', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('categorias', models.ManyToManyField(help_text='Seleccione las categorias', to='blog.Categoria')),
            ],
            options={
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
                'ordering': ['-f_pub'],
            },
        ),
    ]