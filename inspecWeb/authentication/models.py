"""Users Model."""

from django.db import models
from django.contrib.auth.models import User


class InspecUser(models.Model, User):
    """Inspec User."""

    user_cpf = models.CharField(max_lenght=11)
    user_registration = models.CharField(max_lenght=7)
    user_birthday = models.DateTimeField('Ano de Nascimento')
    user_sex = models.CharField(max_lenght=10)
    process_track = models.ManyToMany('Acompanhamento')


class InspecUserAgent(models.Model, User):
    """Inspec secondary user, Agent."""

    user_registration = models.CharField(max_lenght=7)
    public_location = models.ForeignKey('Logradouro')
