"""Document models."""

from django.db import models
from authentication.models import InspecUser, InspecAgent


class Document(models.Model):
    """Abstract document model."""

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)


class Undersigned(Document):
    """Concrete class inherits from document."""

    # signers = models.ManyToManyField(InspecUser)
    status = models.CharField(max_length=100)
    interested = models.ForeignKey(InspecAgent, null=True)

    # def get_signers():
    #     """Get the signers to inform the status of this document."""
    #     return None

    def add_observer(self, interested):
        """Add a InspecAgent to the list of observers."""

    def remove_observer(self, interested):
        """Remove a InspecAgent from observers list."""
        # self.interested
        # Implement the logic here

    def save(self, *args, **kwargs):
        """Override of save method."""
        self.signers.notify()
        super(Undersigned, self).save(*args, **kwargs)

    @classmethod
    def related_user(cls, user_id):
        """Search for all documents related with a certain user."""
        return cls.objects.filter(signers_id=user_id)


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
