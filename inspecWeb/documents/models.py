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

    def get_signers():
        """Get the signers to inform the status of this document."""
        return None

    def notify_observer():
        """Notify all observers."""
        return None


class Report(Document):
    """Concrete class inherits from document."""

    responsible = models.ForeignKey(InspecAgent)
