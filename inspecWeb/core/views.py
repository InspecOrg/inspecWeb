"""Views for core module."""

from django.shortcuts import render_to_response
from django.views.generic import View
from django.template import RequestContext
from core.models import Convenio


class SearchConvenios(View):
    """Class View to search Convenios."""

    http_method_names = [u'get']

    def get(self, request):
        """Get method to acess the page."""
        return render_to_response(
            'convenios.html',
            context_instance=RequestContext(request))


class SearchConveniosByUf(View):
    """Class View to search Convenios by Uf."""

    http_method_names = [u'get']

    def get(self, request):
        """Get method to acess the page."""
        uf_query = request.GET['search_uf']

        convenios = Convenio.get_convenio_by_uf()

        return render_to_response(
            'convenios.html',
            locals(),
            context_instance=RequestContext(request))


class SearchConveniosByMunicipio(View):
    """Class View to search Convenios by municipio."""

    http_method_names = [u'get']

    def get(self, request):
        """Get method to acess the page."""
        municipio_query = request.GET['search_municipio']

        return render_to_response(
            'convenios.html',
            locals(),
            context_instance=RequestContext(request))
