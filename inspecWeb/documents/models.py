"""Document models."""

from django.db import models
from authentication.models import InspecUser, InspecAgent


class Document(models.Model):
    """Abstract document model."""

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)


class Undersigned(Document):
    """Concrete class inherits from document."""

    signers = models.ForeignKey(InspecUser)
    status = models.CharField(max_length=100)
    interested = models.ForeignKey(InspecAgent)

    def get_signers():
        """Get the signers to inform the status of this document."""
        return None

    def notify_observer():
        """Notify all observers."""
        return None

    def add_observer(self, interested):
        """Add a InspecAgent to the list of observers."""
        self.interested + interested

    def remove_observer(self, interested):
        """Remove a InspecAgent from observers list."""
        # self.interested
        # Implement the logic here


class Report(Document):
    """Concrete class inherits from document."""

    responsible = models.ForeignKey(InspecAgent)


class DocumentCreator():
    """Factory method for create both report and Undersigned."""

    def create_document(self, choice_number):
        """Factory method for instantiate concret Documents."""
        if choice_number == 1:
                response = Undersigned()
        elif choice_number == 2:
                response = Report()
        else:
            raise exception

        return response
