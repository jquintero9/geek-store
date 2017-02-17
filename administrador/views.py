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

# Create your views here.


class ListaDepartamento(ListView):
    model = Departamento
    template_name = 'administrador/lista_departamentos.html'
    context_object_name = 'lista_departamentos'

    def get_context_data(self, **kwargs):
        context = super(ListaDepartamento, self).get_context_data(**kwargs)
        context['numeros'] = range(10)
        return context


class CrearDepartamento(SuccessMessageMixin, CreateView):
    model = Departamento
    form_class = CrearDepartamentoForm
    template_name = 'administrador/departamento_create_form.html'
    success_url = reverse_lazy('administrador:lista_departamentos')
    success_message = u'Se ha creado el departamento %(nombre)s con éxito'

    '''def post(self, request, *args, **kwargs):
        c = super(CrearDepartamento, self).post(request, *args, **kwargs)
        messages.success(self.request, 'Departamento creado')
        return c
    '''


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

