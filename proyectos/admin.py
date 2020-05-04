from django.contrib import admin
from .models import Categoria, Proyecto, Capitulo

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

class ProyectoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    list_display = ('nombre', 'fecha_creacion')

class CapituloAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    list_display = ('paso', 'numero', 'proyecto', 'fecha_creacion')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Capitulo, CapituloAdmin)