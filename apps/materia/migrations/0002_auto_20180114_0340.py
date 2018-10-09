# Generated by Django 2.0.1 on 2018-01-14 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materia', '0001_initial'),
        ('universidad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horariomateria',
            name='aula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.Aula'),
        ),
        migrations.AddField(
            model_name='horariomateria',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materia.Materia'),
        ),
    ]
