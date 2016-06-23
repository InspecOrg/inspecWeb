"""Urls for core app."""

from django.conf.urls import url
from .views import SearchConvenio, SearchConvenioByUf


urlpatterns = [
    url(r'^search/', SearchConvenioByUf.as_view(), name='searchUf'),
]
