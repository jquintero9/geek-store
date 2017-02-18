from django.conf.urls import url
from .views import \
    (PublisherList,
     CrearDepartamento,
     ListaDepartamento,
     EditarDepartamento,
     EliminarDepartamento,
     home)

from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied

urlpatterns = [
    #url(r'^accounts/login$', LoginAdmin.as_view(), name='login_admin'),
    url(r'^$', home, name='home'),
    url(r'^departamento/crear$', CrearDepartamento.as_view(), name='crear_departamento'),
    url(r'^departamento/lista$', ListaDepartamento.as_view(), name='lista_departamentos'),
    url(r'^departamento/(?P<pk>\d+)/editar$', EditarDepartamento.as_view(), name='editar_departamento'),
    url(r'^departamento/(?P<pk>\d+)/eliminar$', EliminarDepartamento.as_view(), name='eliminar_departamento'),
]