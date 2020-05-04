from django.contrib import admin
from .models import Curso, Alumno

class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_entrada',)
    list_display = ('nombre_curso', 'horario', 'precio', 'fecha_inicio')

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre_alumno', 'apellidos', 'telefono', 'email', 'curso_registrado', 'fecha_inscripcion', 'contactado', 'comenzado_curso', 'segunda_sesion_prueba', 'pago_realizado', 'finalizado_curso')

admin.site.register(Curso, CursoAdmin)
admin.site.register(Alumno, AlumnoAdmin)

