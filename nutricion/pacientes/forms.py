from django import forms
from .models import Paciente, Consulta, Alimento, Menu

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'edad', 'peso', 'altura', 'genero', 'nivel_actividad', 
                  'porcentaje_proteinas', 'porcentaje_carbohidratos', 'porcentaje_grasas']
        widgets = {
            'porcentaje_proteinas': forms.NumberInput(attrs={'step': '0.01'}),
            'porcentaje_carbohidratos': forms.NumberInput(attrs={'step': '0.01'}),
            'porcentaje_grasas': forms.NumberInput(attrs={'step': '0.01'}),
        }

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'imc', 'tmb', 'calorias_diarias', 'carbohidratos', 'proteinas', 'grasas', 'notas']

class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = ['nombre', 'grupo_alimento', 'calorias', 'carbohidratos', 'proteinas', 'grasas', 'porcion_estandar']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['consulta', 'alimento', 'porcion']
