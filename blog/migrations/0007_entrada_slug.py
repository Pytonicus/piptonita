# Generated by Django 3.0.1 on 2020-05-04 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='slug',
            field=models.SlugField(blank=True, max_length=64),
        ),
    ]
