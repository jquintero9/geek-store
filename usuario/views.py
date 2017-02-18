from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Usuario
from cliente.models import Cliente
from .forms import UserForm, UsuarioForm, ClienteForm, LoginForm
from django.contrib.auth.models import Permission

# Create your views here.


class CerrarSesion(View):
    success_url = reverse_lazy('cuentas:iniciar_sesion')

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(self.success_url)


class IniciarSesion(View):
    form_class = None
    template_name = 'usuario/iniciar_sesion.html'
    success_url = reverse_lazy('home_cliente')

    def get(self, request):
        self.form_class = LoginForm()
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        self.form_class = LoginForm(request.POST)

        if self.form_class.is_valid():
            email = self.form_class.cleaned_data.get('email')
            password = self.form_class.cleaned_data.get('password')

            user = authenticate(username=email, password=password)

            if user is not None:
                login(request, user)
                print user.has_perm('cliente.see_profile')
                return HttpResponseRedirect(self.success_url)
            else:
                messages.error(request, u'El usuario no se encuentra registrado.')

        return render(request, self.template_name, {'form': self.form_class})


class RegistroUsuario(View):
    form_user = None
    form_usuario = None
    form_cliente = None
    template_name = 'usuario/registrarse.html'
    success_url = reverse_lazy('cuentas:iniciar_sesion')

    def get(self, request):
        self.form_user = UserForm()
        self.form_usuario = UsuarioForm()
        self.form_cliente = ClienteForm()

        return render(request, self.template_name,
                      {'formUser': self.form_user, 'formUsuario': self.form_usuario, 'formCliente': self.form_cliente})

    def post(self, request):
        self.form_user = UserForm(request.POST)
        self.form_usuario = UsuarioForm(request.POST)
        self.form_cliente = ClienteForm(request.POST)

        if self.form_user.is_valid() and self.form_usuario.is_valid() and self.form_cliente.is_valid():
            user = User.objects.create_user(username=self.form_user.cleaned_data['email'],
                                            password=self.form_user.cleaned_data['password'],
                                            email=self.form_user.cleaned_data['email'],)

            permiso = Permission.objects.get(name='ver perfil')
            user.user_permissions.add(permiso)

            usuario = Usuario(
                identificacion=self.form_usuario.cleaned_data.get('identificacion'),
                nombres=self.form_usuario.cleaned_data.get('nombres'),
                apellidos=self.form_usuario.cleaned_data.get('apellidos'),
                fecha_nacimiento=self.form_usuario.cleaned_data.get('fecha_nacimiento'),
                telefono=self.form_usuario.cleaned_data.get('telefono'),
                user=user
            )
            usuario.save()

            cliente = Cliente(
                usuario=usuario,
                genero=self.form_cliente.cleaned_data.get('genero'),
                direccion=self.form_cliente.cleaned_data.get('direccion'),
                ciudad=self.form_cliente.cleaned_data.get('ciudad')
            )
            cliente.save()

            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name,
                      {'formUser': self.form_user, 'formUsuario': self.form_usuario, 'formCliente': self.form_cliente})

