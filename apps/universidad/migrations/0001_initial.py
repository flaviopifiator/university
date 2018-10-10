# Generated by Django 2.1.2 on 2018-10-10 09:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django_autoslugfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', django_autoslugfield.fields.AutoSlugField(blank=True, max_length=255, null=True, title_field=None, unique=True)),
                ('descripcion', models.TextField()),
                ('ubicacion', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
            },
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_direccion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre de Calle')),
                ('numero_direccion', models.PositiveIntegerField(blank=True, null=True, verbose_name='Número de Calle')),
                ('extra', models.CharField(blank=True, max_length=400, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('slug', django_autoslugfield.fields.AutoSlugField(blank=True, max_length=255, null=True, title_field=None, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('sigla', models.CharField(blank=True, max_length=50, null=True)),
                ('pagina', models.URLField(blank=True, help_text='URL página web', null=True)),
                ('ubicacion', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name': 'Universidad',
                'verbose_name_plural': 'Universidades',
                'ordering': ('nombre', 'sigla'),
            },
        ),
    ]