# Generated by Django 2.1.1 on 2018-10-07 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facultad', '0017_auto_20180930_1810'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='planestudio',
            unique_together={('año', 'carrera')},
        ),
    ]
