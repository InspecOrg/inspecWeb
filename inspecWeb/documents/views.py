"""Views for document app."""

from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.template import RequestContext
# Create your views here.


class CreateDocument(View):
    """Create Document method for both Undersigned and Report."""

    def get(self, request):
        """Get method for CreateDocument."""
        return render_to_response(
            'index.html', context_instance=RequestContext(request))
