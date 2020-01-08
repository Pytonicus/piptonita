from django.contrib import admin
from .models import Categoria, Entrada

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    
class EntradaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    list_display = ('titulo', 'fecha_creacion')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Entrada, EntradaAdmin)