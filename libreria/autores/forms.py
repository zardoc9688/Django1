from django import forms
from .models import Autor

#Crear formulario
class AutorForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Autor

        #especificar los campos
        fields = [
            'nombre',
            'apellido',
            'pais'
        ]