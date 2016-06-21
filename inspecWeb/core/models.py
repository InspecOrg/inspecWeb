from django.db import models

# Create your models here.


class Convenio(models.Model):
    ano_convenio = models.DateField(null=True)
    nr_convenio = models.IntegerField()
    tx_objeto_convenio = models.CharField(max_length=255)
    id_convenio = models.IntegerField(null=True)
    tx_modelidade = models.CharField(max_length=255)
    tx_situacao = models.CharField(max_length=255)
    tx_substituicao = models.CharField(max_length=255, null=True)
    tx_justificativa = models.CharField(max_length=255)
    dt_assinatura = models.DateField(null=True)
    dt_publicacao = models.DateField(null=True)
    id_programa = models.IntegerField()
    assinado = models.BooleanField()
    publicado = models.BooleanField()
