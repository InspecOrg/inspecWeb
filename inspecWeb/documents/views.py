"""Views for document app."""

from django.shortcuts import render_to_response
from django.views.generic import View
from django.template import RequestContext
from documents.models import Undersigned, DocumentCreator
# Create your views here.


class CreateDocument(View):
    """Create Document method for both Undersigned and Report."""

    http_method_names = [u'get', u'post']

    def get(self, request):
        """Get method for CreateDocument."""
        return render_to_response(
            'index.html', context_instance=RequestContext(request))

    def post(self, request):
        """Post method for CreateDocument."""
        document = DocumentCreator.create_document(1)

        document.title = request.POST['title']
        document.description = request.POST['description']
        document.signers = request.user
        document.save()

        return render_to_response(
            'paginaDpsDaCriação.html',
            locals(),
            context_instance=RequestContext(request))


class ShowDocuments(View):
    """Class to show the releted documents."""

    http_method_names = [u'get']

    def get(self, request):
        """Get method for acess Related Documents page."""
        request_user = request.user.id
        related_documents = Undersigned.related_user(request_user)

        return render_to_response(
            'documents.html', locals(),
            context_instance=RequestContext(request))
