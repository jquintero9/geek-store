#!usr/local/bin
# coding: latin-1

from django import forms
from cliente.models import Departamento


class CrearDepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre Departamento', 'class': "input"})
        }

        error_messages = {
            'nombre': {'required': u'�C�al es el nombre del Departamento?',
                       'max_length': u'Has superado el n�mero de caracteres v�lidos.',},
        }


