#!usr/local/bin
# coding: latin-1

from django import forms
from django.core.validators import EmailValidator, RegexValidator
from usuario.models import Usuario, Regex
from cliente.models import Cliente


'''Esta clase representa los campos email y password del formulario para crear los usuairos.'''


class UserForm(forms.Form):
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}),
                             validators=[EmailValidator(message=u'Ingrese una dirección de correo válida.',
                                                        whitelist=['gmail.com', 'hotmail.com', 'utp.edu.co'])])

    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               validators=[RegexValidator(regex=Regex.password, message=Regex.mensaje_password)])

    confirmar_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Password'}))

    def clean_confirmar_password(self):
        password = self.cleaned_data.get('password')
        confirmar_password = self.cleaned_data.get('confirmar_password')

        if not (password == confirmar_password):
            raise forms.ValidationError(message=u'Las Contraseñas no coinciden')

        return confirmar_password


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        include = '__all__'
        exclude = ['user']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        include = '__all__'
        exclude = ['usuario', 'fecha_alta']


class LoginForm(forms.Form):

    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}),
                             validators=[EmailValidator(message=u'Ingrese una dirección de correo válida \
                                                                 example@gmail.com',
                                                        whitelist=['gmail.com', 'hotmail.com', 'utp.edu.co'])])

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))




