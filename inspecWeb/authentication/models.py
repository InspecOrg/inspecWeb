"""Users Model."""

from django.db import models
from django.contrib.auth.models import User


class InspecUser(User):
    """Inspec User."""

    user_cpf = models.CharField(max_length=11)
    user_registration = models.CharField(max_length=7)
    user_birthday = models.DateTimeField('Ano de Nascimento')
    user_sex = models.CharField(max_length=10)
    # process_track = models.ManyToManyField('Acompanhamento')


class InspecUserAgent(User):
    """Inspec secondary user, Agent."""

    user_registration = models.CharField(max_length=7)
    # public_location = models.ForeignKey('Logradouro')
