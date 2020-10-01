from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
                path('', listar_recetas, name='listar_recetas'),
                path('<uuid:pub>/', ver_receta, name='ver_receta'),
                path('categoria/<int:categoria>/', ver_recetas_categoria, name='ver_recetas_categoria')
]



