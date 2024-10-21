from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Consulta
from .forms import PacienteForm
from decimal import Decimal
from django.http import HttpResponseRedirect
from django.urls import reverse

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista_pacientes.html', {'pacientes': pacientes})

def agregar_consulta(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    
    # Usamos la función existente calcular_plan_nutricional para crear la nueva consulta
    consulta = calcular_plan_nutricional(paciente)
    
    # Redirigimos de vuelta a la página de detalles del paciente
    return redirect('detalles_paciente', paciente_id=paciente.id)

def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            consulta = calcular_plan_nutricional(paciente)  # Generar nuevo plan nutricional
            return redirect('detalles_paciente', paciente_id=paciente.id)
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'pacientes/editar_paciente.html', {'form': form, 'paciente': paciente})

def eliminar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    consulta.delete()
    # Redirigir a la página de detalles del paciente
    return HttpResponseRedirect(reverse('detalles_paciente', args=[consulta.paciente.id]))

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/crear_paciente.html', {'form': form})

def vista_principal(request):
    pacientes = Paciente.objects.all()  # Obtiene todos los pacientes
    return render(request, 'pacientes/vista_principal.html', {'pacientes': pacientes})

def detalles_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    consultas = Consulta.objects.filter(paciente=paciente)

    # Remover el cálculo al cargar detalles del paciente
    # Si quieres calcular el plan solo en la edición
    if request.method == 'POST':
        return redirect('detalles_paciente', paciente_id=paciente.id)  # Redirigir para evitar múltiples envíos

    return render(request, 'pacientes/detalles_paciente.html', {
        'paciente': paciente,
        'consultas': consultas,
    })

def calcular_imc(peso, altura_cm):
    altura_m = altura_cm / 100  # Convierte la altura de cm a metros
    if altura_m > 0:  # Asegúrate de que la altura no sea cero para evitar errores
        imc = peso / (altura_m ** 2)  # Fórmula del IMC
        return round(imc, 1)  # Redondear a un decimal
    return 0  # Retornar 0 si la altura es cero o inválida

def calcular_plan_nutricional(paciente):
    peso = Decimal(paciente.peso)  # Asegúrate de que esto sea Decimal
    altura = Decimal(paciente.altura)  # Asegúrate de que esto sea Decimal
    edad = paciente.edad
    genero = paciente.genero
    nivel_actividad = paciente.nivel_actividad

    # 2. Calcular la Tasa Metabólica Basal (TMB)
    if genero == 'M':
        tmb = (Decimal(10) * peso) + (Decimal(6.25) * altura) - (Decimal(5) * Decimal(edad)) + Decimal(5)
    else:
        tmb = (Decimal(10) * peso) + (Decimal(6.25) * altura) - (Decimal(5) * Decimal(edad)) - Decimal(161)

    # 3. Ajustar el TMB según el nivel de actividad
    if nivel_actividad == 'Sedentario':
        calorias_diarias = tmb * Decimal(1.2)
    elif nivel_actividad == 'Ligera':
        calorias_diarias = tmb * Decimal(1.375)
    elif nivel_actividad == 'Moderada':
        calorias_diarias = tmb * Decimal(1.55)
    else:  # Intensa
        calorias_diarias = tmb * Decimal(1.725)

    # 4. Calcular distribución de macronutrientes
    porcentaje_proteinas = paciente.porcentaje_proteinas / Decimal(100)
    porcentaje_carbohidratos = paciente.porcentaje_carbohidratos / Decimal(100)
    porcentaje_grasas = paciente.porcentaje_grasas / Decimal(100)

    calorias_proteinas = calorias_diarias * porcentaje_proteinas
    calorias_carbohidratos = calorias_diarias * porcentaje_carbohidratos
    calorias_grasas = calorias_diarias * porcentaje_grasas

    # 5. Convertir calorías a gramos
    gramos_proteinas = calorias_proteinas / Decimal(4)  # 1 g de proteína = 4 kcal
    gramos_carbohidratos = calorias_carbohidratos / Decimal(4)  # 1 g de CHO = 4 kcal
    gramos_grasas = calorias_grasas / Decimal(9)  # 1 g de grasa = 9 kcal

    # 6. Guardar los resultados en la base de datos (Consulta)
    consulta = Consulta(
        paciente=paciente,
        imc=calcular_imc(paciente.peso, paciente.altura),  # Asumiendo que tienes esta función
        tmb=Decimal(tmb),
        calorias_diarias=Decimal(calorias_diarias),
        carbohidratos=Decimal(gramos_carbohidratos),
        proteinas=Decimal(gramos_proteinas),
        grasas=Decimal(gramos_grasas)
    )
    consulta.save()

    return consulta