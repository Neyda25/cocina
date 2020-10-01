from django.shortcuts import render

from .models import *


def listar_recetas(request):
    news = Receta.objects.all().order_by('-f_pub')
    return render(request, './post/index.html', {'news':news})


def ver_receta(request, pub):
    publicacion = Receta.objects.get(id = pub)
    return render(request, './post/ver.html', {'pub':publicacion})


def ver_recetas_categoria(request, categoria):
    categoria = Categoria.objects.get(id= categoria)
    return render(request,'./post/index.html', {'categoria':categoria})

