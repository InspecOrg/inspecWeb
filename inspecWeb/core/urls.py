"""Urls for core app."""

from django.conf.urls import url
from .views import ViewConvenios, SearchConvenios


urlpatterns = [
    url(r'^search/',
        SearchConvenios.as_view(), name='searchUf'),
    url(r'^convenios/', ViewConvenios.as_view(), name='Convenios')
]
