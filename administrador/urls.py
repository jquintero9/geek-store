from django.conf.urls import url
from .views import PublisherList

urlpatterns = [
    url(r'^publisher/$', PublisherList.as_view(), name='publisher')
]