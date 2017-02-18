from django.conf.urls import url
from .views import RegistroUsuario, IniciarSesion, CerrarSesion

urlpatterns = [
    #url(r'^login$'),
    url(r'^signup$', RegistroUsuario.as_view(), name='registrarse'),
    url(r'^login$', IniciarSesion.as_view(), name='iniciar_sesion'),
    url(r'^logout$', CerrarSesion.as_view(), name='cerrar_sesion'),
]