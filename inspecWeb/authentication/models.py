"""Users Model."""

from django.db import models
from django.contrib.auth.models import User


class InspecUser(User):
    """Inspec User."""

    user_cpf = models.CharField(max_length=11)
    user_registration = models.CharField(max_length=7)
    user_birthday = models.DateTimeField(auto_now=True)
    user_gender = models.CharField(max_length=10)
    process_track = models.ManyToManyField('Acompanhamento')


class InspecAgent(User):
    """Inspec secondary user, Agent."""

    agent_registration = models.CharField(max_length=7)
    public_location = models.ForeignKey('Logradouro')


class Acompanhamento(models.Model):
    """relation of InspecUser and public_concession."""

    related_user = models.ForeignKey('InspecUser')
    # public_concession = models.ForeignKey('Convenio')


class Logradouro(models.Model):
    """Public_location attr."""

    place_name = models.CharField(max_length=100)
    place_adress = models.CharField(max_length=100)
    place_phone_number = models.CharField(max_length=10)
