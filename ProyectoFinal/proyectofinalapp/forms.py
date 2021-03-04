from django.forms import ModelForm
from .models import Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['titulo', 'texto', 'direccion','ubicacion','telefono','imagen','website', 'autor']