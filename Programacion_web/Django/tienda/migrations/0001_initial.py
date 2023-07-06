# Generated by Django 4.2.3 on 2023-07-05 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id_tipo', models.AutoField(db_column='idTipo', primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=45)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.IntegerField()),
                ('id_tipo', models.ForeignKey(db_column='idTipo', on_delete=django.db.models.deletion.CASCADE, to='tienda.tipo')),
            ],
        ),
    ]
