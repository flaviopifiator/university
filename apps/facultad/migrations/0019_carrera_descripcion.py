# Generated by Django 2.1.1 on 2018-10-08 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultad', '0018_auto_20181007_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
