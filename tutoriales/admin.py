from django.contrib import admin
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_edicion')
    list_display = ('nombre', 'descripcion', 'fecha_creacion')

admin.site.register(Tutorial, TutorialAdmin)
