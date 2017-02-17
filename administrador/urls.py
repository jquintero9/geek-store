from django.conf.urls import url
from .views import PublisherList, CrearDepartamento, ListaDepartamento, EditarDepartamento, EliminarDepartamento

urlpatterns = [
    url(r'^departamento/crear$', CrearDepartamento.as_view(), name='crear_departamento'),
    url(r'^departamento/lista$', ListaDepartamento.as_view(), name='lista_departamentos'),
    url(r'^departamento/(?P<pk>\d+)/editar$', EditarDepartamento.as_view(), name='editar_departamento'),
    url(r'^departamento/(?P<pk>\d+)/eliminar$', EliminarDepartamento.as_view(), name='eliminar_departamento'),
]