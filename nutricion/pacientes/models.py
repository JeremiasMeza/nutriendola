from django.db import models

# Create your models here.
from django.db import models

# pacientes/models.py
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    nivel_actividad = models.CharField(max_length=50, default='Sedentario', choices=[('Sedentario', 'Sedentario'), ('Ligera', 'Ligera'), ('Moderada', 'Moderada'), ('Intensa', 'Intensa')])
    
    # Nuevos campos para porcentajes de macronutrientes
    porcentaje_proteinas = models.DecimalField(max_digits=5, decimal_places=2, default=20.0)  # 20%
    porcentaje_carbohidratos = models.DecimalField(max_digits=5, decimal_places=2, default=50.0)  # 50%
    porcentaje_grasas = models.DecimalField(max_digits=5, decimal_places=2, default=30.0)  # 30%

    def __str__(self):
        return self.nombre


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imc = models.DecimalField(max_digits=5, decimal_places=2)
    tmb = models.DecimalField(max_digits=7, decimal_places=2)
    calorias_diarias = models.DecimalField(max_digits=7, decimal_places=2)
    carbohidratos = models.DecimalField(max_digits=7, decimal_places=2)
    proteinas = models.DecimalField(max_digits=7, decimal_places=2)
    grasas = models.DecimalField(max_digits=7, decimal_places=2)
    notas = models.TextField(null=True, blank=True)

class Alimento(models.Model):
    nombre = models.CharField(max_length=100)
    grupo_alimento = models.CharField(max_length=50)
    calorias = models.DecimalField(max_digits=7, decimal_places=2)
    carbohidratos = models.DecimalField(max_digits=7, decimal_places=2)
    proteinas = models.DecimalField(max_digits=7, decimal_places=2)
    grasas = models.DecimalField(max_digits=7, decimal_places=2)
    porcion_estandar = models.DecimalField(max_digits=7, decimal_places=2)

class Menu(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    porcion = models.DecimalField(max_digits=7, decimal_places=2)
