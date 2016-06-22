from django.db import models

# Create your models here.


class Convenio(models.Model):
    ano_convenio = models.DateField(null=True)
    nr_convenio = models.IntegerField(null=True)
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

    @classmethod
    def get_convenio_by_municipio(cls, municipio):
        """Get all instances of 'Convenio' by municipio query."""
        return cls.objetcs.filter(
            nm_municipio_proponente__startswith=municipio)

    @classmethod
    def get_convenio_by_region(cls, regiao):
        """Get all instances of 'Convenio' that matches region query."""
        return cls.objetcs.filter(tx_region_proponente__startswith=regiao)

    @classmethod
    def get_convenio_by_uf(cls, uf):
        u"""Get all instances of 'Convenio' that matches(Unidade da Federação)."""
        return cls.objetcs.filter(uf_proponente__startswith=uf)
