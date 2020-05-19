from django.db import models
from django.urls import reverse

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=200, verbose_name="Nombre del curso")
    imagen_curso = models.ImageField(upload_to="cursos/imagenes/", verbose_name="Imagen del curso")
    horario = models.CharField(max_length=200, verbose_name="Horario del curso")
    precio = models.CharField(max_length=50, verbose_name="Precio del curso")
    requisitos = models.CharField(max_length=200, verbose_name="Requisitos")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_entrada = models.DateTimeField(auto_now=True, verbose_name="Añadido el")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-fecha_entrada']

    def __str__(self):
        return self.nombre_curso

    def get_absolute_url(self):
        return reverse('curso', kwargs={'pk':self.pk})

class Alumno(models.Model):
    nombre_alumno = models.CharField(max_length=200, verbose_name="Nombre del Alumno")
    apellidos = models.CharField(max_length=200, verbose_name="Apellidos")
    edad = models.IntegerField(verbose_name="Edad (mayor de 18)")
    telefono = models.CharField(max_length=20, verbose_name="Número de teléfono")
    email = models.EmailField(verbose_name="Dirección de email")
    provincia = models.CharField(max_length=100, verbose_name="Provincia (España)")
    curso_registrado = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    fecha_inscripcion = models.DateTimeField(auto_now=True, verbose_name="Fecha de inscripción")
    contactado = models.BooleanField(default=False)
    comenzado_curso = models.BooleanField(default=False)
    segunda_sesion_prueba = models.BooleanField(default=False)
    pago_realizado = models.BooleanField(default=False)
    finalizado_curso = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ['-fecha_inscripcion']

    def __str__(self):
        return self.nombre_alumno