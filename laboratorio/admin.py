from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_entrada',)
    list_display = ('nombre_lab', 'horario', 'fecha_inicio')

admin.site.register(Curso, CursoAdmin)
