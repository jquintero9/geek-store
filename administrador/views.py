#!usr/local/bin
# coding: latin-1

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Publisher, Author, Book
from django.shortcuts import get_object_or_404

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cliente.models import Departamento
from .forms import CrearDepartamentoForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from usuario.forms import LoginForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
# Create your views here.


@login_required(login_url=reverse_lazy('administrador:login_admin'))
def home(request):
    if request.user.has_perm('administrador.es_administrador'):
        return render(request, 'administrador/home.html', {})
    else:
        raise PermissionDenied


'''class LoginAdmin(View):

    template_name = 'administrador/login.html'
    form = None
    success_url = reverse_lazy('administrador:home')

    def get(self, request):
        self.form = LoginForm()
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        self.form = LoginForm(request.POST)
        if self.form.is_valid():
            user = authenticate(username=self.form.cleaned_data['email'],
                                password=self.form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(self.success_url)
                else:
                    messages.warning(request, u'La cuenta de este usuario no está activada.')
            else:
                messages.error(request, u'El correo y/o la contraseña son incorrectos.')

        return render(request, self.template_name, {'form': self.form})
'''

class ListaDepartamento(ListView):
    model = Departamento
    template_name = 'administrador/lista_departamentos.html'
    context_object_name = 'lista_departamentos'

    def get_context_data(self, **kwargs):
        context = super(ListaDepartamento, self).get_context_data(**kwargs)
        context['numeros'] = range(10)
        return context


class CrearDepartamento(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Departamento
    form_class = CrearDepartamentoForm
    template_name = 'administrador/departamento_create_form.html'
    success_url = reverse_lazy('administrador:lista_departamentos')
    success_message = u'Se ha creado el departamento %(nombre)s con éxito'
    login_url = reverse_lazy('administrador:login_admin')

    def get(self, request, *args, **kwargs):
        if request.user.has_perm('administrador.es_administrador'):
            return super(CrearDepartamento, self).get(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def post(self, request, *args, **kwargs):
        if request.user.has_perm('administrador.es_administrador'):
            return super(CrearDepartamento, self).post(request, *args, **kwargs)
        else:
            raise PermissionDenied


class EliminarDepartamento(DeleteView):
    model = Departamento
    template_name = 'administrador/eliminar_departamento.html'
    success_url = reverse_lazy('administrador:lista_departamentos')


class EditarDepartamento(UpdateView):
    model = Departamento
    form_class = CrearDepartamentoForm
    template_name = 'administrador/departamento_create_form.html'
    success_url = reverse_lazy('administrador:lista_departamentos')



class PublisherList(ListView):
    model = Publisher
    template_name = 'publisher_list.html'
    context_object_name = 'publisher_list'


class PublisherFilter(ListView):
    model = Publisher
    template_name = 'publisher_list.html'
    context_object_name = 'publisher_list'

    def get_queryset(self):
        print self.args[0]
        self.editorial = get_object_or_404(Publisher, name=self.args[0])
        return self.editorial

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherFilter, self).get_context_data(**kwargs)
        # Add in the publisher
        context['editorial'] = self.editorial
        return context

class PublisherDetail(DetailView):

    model = Publisher
    template_name = 'publisher_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context

