# Generated by Django 5.0.6 on 2024-05-31 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bitacora', '0004_alter_loginuser_linea_alter_loginuser_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='linea',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='turno',
            field=models.CharField(max_length=12),
        ),
    ]
