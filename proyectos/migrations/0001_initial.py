# Generated by Django 3.0.1 on 2020-02-27 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Tecnología')),
                ('fecha_creacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Tecnología',
                'verbose_name_plural': 'Tecnologías',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre del Proyecto')),
                ('imagen', models.ImageField(upload_to='proyectos/imagenes/', verbose_name='Imagen')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.Categoria', verbose_name='Tecnología')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paso', models.CharField(max_length=150, verbose_name='Paso')),
                ('video', models.URLField(verbose_name='Ruta del video')),
                ('transcripcion', models.TextField(verbose_name='Transcripción')),
                ('pdf', models.FileField(upload_to='proyectos/pdfs/')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualización')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.Proyecto', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Paso',
                'verbose_name_plural': 'Pasos',
                'ordering': ['paso'],
            },
        ),
    ]