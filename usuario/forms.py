#!usr/local/bin
# coding: latin-1

from django import forms
from django.core.validators import EmailValidator, RegexValidator
from .models import Usuario
from cliente.models import Cliente

'''Esta clase contiene las expresiones regulares que ser�n utlizadas
para validar los campos de los formularios.'''


class Regex(object):
    password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&#\-_])[A-Za-z\d$@$!%*?&#\-_]{8,16}'
    mensaje_password = u'La contrase�a debe tener m�ximo un caracter \
    especial($@$!%*?&), una minusc�la, una mayusc�la y un d�gito.'
    texto = r'^[A-Za-z����������\s]+$'
    mensaje_texto = u'Este campo solo admite letras.'
    telefono = r'^[3]([0][0-5]|[1][0-9]|[2][0-2]|[5][01])[\d]{7}$'
    mensaje_telefono = u'El n�mero de celular ingresado no es v�lido.'

'''Esta clase representa los campos email y password del formulario para crear los usuairos.'''


class UserForm(forms.Form):
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}),
                             validators=[EmailValidator(message=u'Ingrese una direcci�n de correo v�lida.',
                                                        whitelist=['gmail.com', 'hotmail.com', 'utp.edu.co'])])

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               validators=[RegexValidator(regex=Regex.password, message=Regex.mensaje_password)])


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        include = '__all__'
        exclude = ['user']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        include = ['genero', 'direccion', 'ciudad']




