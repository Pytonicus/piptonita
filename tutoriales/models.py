from django.db import models

class Tutorial(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Tutorial")
    imagen = models.ImageField(upload_to="tutoriales/imagenes/", verbose_name="Imagen")
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    video = models.URLField(verbose_name="Video")
    transcripcion = models.TextField(verbose_name="Transcripción")
    archivoPdf = models.FileField(upload_to="tutoriales/pdfs/")

    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="Tutorial"
        verbose_name_plural="Tutoriales"
        ordering=["-fecha_creacion"]
    
    def __str__(self):
        return self.nombre
    