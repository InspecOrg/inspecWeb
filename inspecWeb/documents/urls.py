"""Urls for document app."""

from django.conf.urls import url
from .views import CreateDocument


urlpatterns = [
    url(r'^unsigned/(?P<convenio_id>[0-9]+)/$', CreateDocument.as_view(),
        name='document')
]
