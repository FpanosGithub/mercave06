# Generated by Django 4.0.4 on 2022-05-05 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercave', '0003_circulacion_pfinal_circulacion_pinicio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circulacion',
            name='loc_final',
        ),
        migrations.RemoveField(
            model_name='circulacion',
            name='loc_inicio',
        ),
    ]
