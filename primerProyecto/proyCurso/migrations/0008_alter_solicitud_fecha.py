# Generated by Django 4.1.3 on 2022-12-17 03:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyCurso', '0007_solicitud_codigosolicitud_alter_solicitud_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2022, 12, 17, 3, 26, 27, 564664)),
        ),
    ]