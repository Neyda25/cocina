from django.contrib import admin

from .models import *


class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido', 'autor', 'f_pub')
    readonly_fields=['f_pub']



admin.site.register(Categoria,)
admin.site.register(Receta, RecetaAdmin)
