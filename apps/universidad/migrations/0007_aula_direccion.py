# Generated by Django 2.1.1 on 2018-09-29 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universidad', '0006_auto_20180114_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='direccion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
