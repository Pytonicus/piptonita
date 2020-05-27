from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Tecnología")
    fecha_creacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="Tecnología"
        verbose_name_plural="Tecnologías"
        ordering = ["nombre"]
    
    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Proyecto")
    imagen = models.ImageField(upload_to="proyectos/imagenes/", verbose_name="Imagen")
    descripcion = models.TextField(verbose_name="Descripción")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Tecnología")

    fecha_creacion = models.DateField(auto_now=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
        ordering = ["nombre"]
    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('proyecto', kwargs={'pk': self.pk})

class Capitulo(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, verbose_name="Proyecto")
    paso = models.CharField(max_length=150, verbose_name="Paso")
    numero = models.IntegerField(verbose_name="Numero del paso")
    video = models.URLField(verbose_name="Ruta del video")
    transcripcion = models.TextField(verbose_name="Transcripción")
    pdf = models.FileField(upload_to="proyectos/pdfs/")

    fecha_creacion = models.DateField(auto_now=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="Paso"
        verbose_name_plural="Pasos"
        ordering = ["numero"]
    
    def __str__(self):
        return self.paso



