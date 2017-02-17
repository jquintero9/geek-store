"""geek_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from administrador.views import PublisherList,PublisherDetail, PublisherFilter

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'accounts/', include('usuario.urls_cuentas', namespace='cuentas')),
    url(r'^administrador/', include('administrador.urls', namespace='administrador')),
    url(r'^cliente/', include('cliente.urls', namespace='cliente')),
    url(r'^publisher/$', PublisherList.as_view(), name='publisher'),
    url(r'^publisher/([\w-]+)/$', PublisherFilter.as_view()),
]
