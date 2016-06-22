"""Views for document app."""

from django.shortcuts import render_to_response
from django.views.generic import View
from django.template import RequestContext
from documents.models import Undersigned
# Create your views here.


class CreateDocument(View):
    """Create Document method for both Undersigned and Report."""

    def get(self, request):
        """Get method for CreateDocument."""
        return render_to_response(
            'index.html', context_instance=RequestContext(request))

    def post(self, request):
        """Post method for CreateDocument."""
        return None


class ShowDocuments(View):
    """Class to show the releted documents."""

    def get(self, request):
        """Get method for acess Related Documents page."""
        request_user = request.user.id
        related_documents = Undersigned.related_user(request_user)

        return render_to_response(
            'documents.html', locals(),
            context_instance=RequestContext(request))
