# Generated by Django 5.1.2 on 2024-10-21 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('grupo_alimento', models.CharField(max_length=50)),
                ('calorias', models.DecimalField(decimal_places=2, max_digits=7)),
                ('carbohidratos', models.DecimalField(decimal_places=2, max_digits=7)),
                ('proteinas', models.DecimalField(decimal_places=2, max_digits=7)),
                ('grasas', models.DecimalField(decimal_places=2, max_digits=7)),
                ('porcion_estandar', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('imc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tmb', models.DecimalField(decimal_places=2, max_digits=7)),
                ('calorias_diarias', models.DecimalField(decimal_places=2, max_digits=7)),
                ('carbohidratos', models.DecimalField(decimal_places=2, max_digits=7)),
                ('proteinas', models.DecimalField(decimal_places=2, max_digits=7)),
                ('grasas', models.DecimalField(decimal_places=2, max_digits=7)),
                ('notas', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=10)),
                ('nivel_actividad', models.CharField(choices=[('Sedentario', 'Sedentario'), ('Ligera', 'Ligera'), ('Moderada', 'Moderada'), ('Intensa', 'Intensa')], default='Sedentario', max_length=50)),
                ('porcentaje_proteinas', models.DecimalField(decimal_places=2, default=20.0, max_digits=5)),
                ('porcentaje_carbohidratos', models.DecimalField(decimal_places=2, default=50.0, max_digits=5)),
                ('porcentaje_grasas', models.DecimalField(decimal_places=2, default=30.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcion', models.DecimalField(decimal_places=2, max_digits=7)),
                ('alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.alimento')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.consulta')),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente'),
        ),
    ]
