"""Views for document app."""

from django.shortcuts import render_to_response, redirect
from django.views.generic import View
from django.template import RequestContext
from documents.models import Undersigned, DocumentCreator, Document
from core.models import Convenio
from authentication.models import InspecUser
# Create your views here.


class CreateDocument(View):
    """Create Document method for both Undersigned and Report."""

    http_method_names = [u'get']

    def get(self, request, convenio_id):
        """Get method for CreateDocument."""
        convenio = Convenio.objects.get(id=convenio_id)

        convenio_nm = convenio.programa.nm_programa

        document = Undersigned.objects.get_or_none(title__contains=convenio_nm)

        if document is None:
            document = DocumentCreator.create_document(1)

            document.title = (
                "Abaixo-Assinado para " + convenio.programa.nm_programa)
            document.description = (
                "Orgão Responsavel pela concessão " + \
                convenio.superior.nm_orgao_superior + \
                "\nEntidade Proponente: "+convenio.proponente.nm_proponente + \
                "\n UF -" + convenio.proponente.uf_proponente )

            document.save()
            document.signers.add(request.user)
        else:
            user = InspecUser.objects.get(id=request.user.id)
            document.signers.add(user)
            document.save()



        return redirect('/index/')

    # def post(self, request):
    #     """Post method for CreateDocument."""
    #     document = DocumentCreator.create_document(1)

    #     document.title = request.POST['title']
    #     document.description = request.POST['description']
    #     document.signers = request.user
    #     document.save()

    #     return render_to_response(
    #         'paginaDpsDaCriação.html',
    #         locals(),
    #         context_instance=RequestContext(request))


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
