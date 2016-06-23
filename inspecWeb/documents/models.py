"""Document models."""

from django.db import models
from authentication.models import InspecAgent, InspecUser
from core.models import InspecModel
from django.db.models.signals import m2m_changed


class Document(InspecModel):
    """Abstract document model."""

    title = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=500, null=True)
    inspecusers = models.ManyToManyField('authentication.InspecUser')

    def __str__(self):
        return "{} - {}".format(self.title, self.description)


class Undersigned(Document):
    """Concrete class inherits from document."""

    status = models.CharField(max_length=100, null=True)
    signers = models.ManyToManyField('authentication.InspecUser')

    # def get_signers():
    #     """Get the signers to inform the status of this document."""
    #     return None

    def add_observer(self, interested):
        """Add a InspecAgent to the list of observers."""

    def remove_observer(self, interested):
        """Remove a InspecAgent from observers list."""
        # self.interested
        # Implement the logic here

    @classmethod
    def related_user(cls, user_id):
        """Search for all documents related with a certain user."""
        return cls.objects.filter(signers_id=user_id)


def undersigned_changed(sender, **kwargs):
    import ipdb
    ipdb.set_trace()
    try:
        instance = kwargs.pop('instance', None)
        und = instance
        user = und.signers.last()
        user.notify()
        print('sendind email')
    except:
        print('first user')
        pass

m2m_changed.connect(undersigned_changed, sender=Undersigned.signers.through)


class Report(Document):
    """Concrete class inherits from document."""

    responsible = models.ForeignKey(InspecAgent)


class DocumentCreator():
    """Factory method for create both report and Undersigned."""

    @classmethod
    def create_document(cls, choice_number):
        """Factory method for instantiate concret Documents."""
        if choice_number == 1:
                response = Undersigned()
        elif choice_number == 2:
                response = Report()
        else:
            pass

        return response
