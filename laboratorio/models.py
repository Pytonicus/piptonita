from django.db import models
from django.urls import reverse

class Curso(models.Model):
    nombre_lab = models.CharField(max_length=200, verbose_name="Nombre del evento")
    imagen_lab = models.ImageField(upload_to="cursos/imagenes/", verbose_name="Imagen del evento")
    resumen = models.CharField(max_length=200, verbose_name="Resumen")
    horario = models.CharField(max_length=200, verbose_name="Horario del evento")
    requisitos = models.CharField(max_length=200, verbose_name="Requisitos")
    descripcion = models.TextField(verbose_name="Descripción")
    link_video = models.URLField(verbose_name="Link de la sesion", blank=True)
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_entrada = models.DateTimeField(auto_now=True, verbose_name="Añadido el")

    class Meta:
        verbose_name = "Laboratorio"
        verbose_name_plural = "Eventos"
        ordering = ['-fecha_entrada']

    def __str__(self):
        return self.nombre_lab

    def get_absolute_url(self):
        return reverse('nombre_lab', kwargs={'pk':self.pk})
