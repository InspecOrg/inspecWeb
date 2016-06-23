"""Urls for core app."""

from django.conf.urls import url
from .views import ViewConvenios, SearchConvenios, ShowConveniosDetail


urlpatterns = [
    url(r'^search/',
        SearchConvenios.as_view(), name='searchUf'),
    url(r'^convenios/', ViewConvenios.as_view(), name='Convenios'),
    url(r'^convenio/(?P<convenio_id>[0-9]+)/$', ShowConveniosDetail.as_view(),
        name="convenio_detail")
]
