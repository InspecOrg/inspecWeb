"""Views for core module."""

from django.shortcuts import render_to_response
from django.views.generic import View
from django.template import RequestContext
from core.models import Convenio


class ViewConvenios(View):
    """Class View to search Convenios."""

    http_method_names = [u'get']

    def get(self, request):
        """Get method to acess the page."""
        convenios = Convenio.objects.all()
        return render_to_response(
            'convenios.html',
            locals(),
            context_instance=RequestContext(request))


class SearchConvenios(View):
    """Class View to search Convenios by Uf."""

    http_method_names = [u'get']

    def get(self, request):
        """Get method to acess the page."""
        query = request.GET['search']

        convenios = Convenio.get_convenio_by_uf(query)

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

        convenios = Convenio.get_convenio_by_municipio(municipio_query)

        return render_to_response(
            'convenios.html',
            locals(),
            context_instance=RequestContext(request))
