#!usr/local/bin
# coding: latin-1

from django.shortcuts import render
from django.views.generic import DetailView
from django.views import View
from .models import Cliente
from usuario.models import Usuario
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import Http404
from django.core.exceptions import PermissionDenied


def home(request):
    return render(request, 'home_cliente.html', {})


'''
class DetailCliente(DetailView):
    template_name = 'perfil_cliente.html'
    context_object_name = 'cliente'
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super(DetailCliente, self).get_context_data(**kwargs)
        return context
'''


#@permission_required('cliente.see_profile')
class PerfilCliente(View):

    template = 'perfil_cliente.html'
    cliente = None

    def get(self, request):
        if request.user.has_perm('cliente.see_profile'):

            try:
                usuario = Usuario.objects.get(user=request.user)
                self.cliente = Cliente.objects.get(usuario=usuario)
            except Exception:
                raise Http404(u'El Cliente no existe')
        else:
            raise PermissionDenied

        return render(request, self.template, {'cliente': self.cliente})
