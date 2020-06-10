from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Categoría")

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Entrada(models.Model):
    titulo = models.CharField(max_length=100, unique=True, verbose_name="Título")
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Autor")
    imagen = models.ImageField(upload_to="entradas/", blank=True)
    contenido = models.TextField(verbose_name="Contenido", null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")
    enlace = models.URLField(verbose_name="Enlace a entrada", blank=True)

    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-fecha_creacion"]
    
    def __str__(self):
        return self.titulo
