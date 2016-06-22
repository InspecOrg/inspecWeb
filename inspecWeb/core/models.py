from django.db import models
from abc import abstractmethod


class ServicoBuilder(models.Model):

    @abstractmethod
    def build_proponente():
        raise NotImplementedError()

    @abstractmethod
    def build_concedente():
        raise NotImplementedError()

    @abstractmethod
    def build_datas():
        raise NotImplementedError()

    @abstractmethod
    def build_responsavel():
        raise NotImplementedError()

    @abstractmethod
    def build_valores():
        raise NotImplementedError()

    @abstractmethod
    def build_superior():
        raise NotImplementedError()

    @abstractmethod
    def gerar_servico():
        raise NotImplementedError()


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

    concedente = models.ForeignKey('Concedente', null=True)
    datas = models.ForeignKey('Datas', null=True)
    programa = models.ForeignKey('Programa', null=True)
    proponente = models.ForeignKey('Proponente', null=True)
    proposta = models.ForeignKey('Proposta', null=True)
    superior = models.ForeignKey('Superior', null=True)
    valores = models.ForeignKey('Valores', null=True)


class Concedente(models.Model):
    nm_respons_concedente = models.CharField(max_length=255, null=True)
    cd_respons_concedente = models.FloatField(default=0.0)
    nm_orgao_concedente = models.CharField(max_length=255, null=True)
    cd_orgao_concedente = models.FloatField(default=0.0)


class Datas(models.Model):
    ano_convenio = models.DateField(null=True)
    dt_inicio_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField()
    dt_assinatura = models.DateField(null=True)
    dt_publicacao = models.DateField(null=True)


class Programa(models.Model):
    cd_programa = models.FloatField(default=0.0)
    nm_programa = models.CharField(max_length=255, null=True)
    cd_acao_programa = models.IntegerField(null=True)


class Proponente(models.Model):
    cd_identif_proponente = models.CharField(max_length=255)
    nm_proponente = models.CharField(max_length=255, null=True)
    tx_esfera_adm_proponente = models.CharField(max_length=255, null=True)
    tx_regiao_proponente = models.CharField(max_length=255, null=True)
    uf_proponente = models.CharField(max_length=255, null=True)
    nm_municipio_proponente = models.CharField(max_length=255, null=True)
    tx_qualific_proponente = models.CharField(max_length=255, null=True)
    nm_respons_proponente = models.CharField(max_length=255, null=True)
    cd_repons_proponente = models.FloatField(default=0.0)


class Proposta(models.Model):
    ano_proposta = models.DateField(null=True)
    nr_proposta = models.IntegerField(null=True)
    dt_proposta = models.DateField(null=True)
    id_proposta = models.IntegerField(null=True)


class Responsavel(models.Model):
    nm_respons_proponente = models.CharField(max_length=255, null=True)
    cd_respons_proponente = models.FloatField(default=0.0)
    nm_respons_concedente = models.CharField(max_length=255, null=True)
    cd_respons_concedente = models.FloatField(default=0.0, null=True)


class Superior(models.Model):
    nm_orgao_superior = models.CharField(max_length=255)
    cd_orgao_superior = models.IntegerField()


class Valores(models.Model):
    # value = "R$ 50,00"
    # value = value[:-3]
    # value = sub(r'[^\d.]', '', value)
    # value = value.replace('.','')
    # value = int(value)

    vl_global = models.IntegerField(null=True)
    vl_repasse = models.IntegerField(null=True)
    vl_repasse_exerc_atual = models.IntegerField(null=True)
    vl_contrapartida = models.IntegerField(null=True)
    vl_contrapartida_financ = models.IntegerField(null=True)
    vl_contrapartida_bens_serv = models.IntegerField(null=True)


class ConvenioBuilder(ServicoBuilder):
    convenio = Convenio()
    concedente = Concedente()
    datas = Datas()
    programa = Programa()
    proponente = Proponente()
    proposta = Proposta()
    responsavel = Responsavel()
    superior = Superior()
    valores = Valores()

    def build_valores(self, vl_global, vl_repasse, vl_repasse_exerc_atual,
                      vl_contrapartida, vl_contrapartida_financ,
                      vl_contrapartida_bens_serv):
        self.valores.vl_global = vl_global
        self.valores.vl_repasse = vl_repasse
        self.valores.vl_repasse_exerc_atual = vl_repasse_exerc_atual
        self.valores.vl_contrapartida = vl_contrapartida
        self.valores.vl_contrapartida_financ = vl_contrapartida_financ
        self.valores.vl_contrapartida_bens_serv = vl_contrapartida_bens_serv

    def build_superior(self, nm_orgao_superior, cd_orgao_superior):
        self.superior.nm_orgao_superior = nm_orgao_superior
        self.superior.cd_orgao_superior = cd_orgao_superior

    def build_responsavel(self, nm_respons_proponente, cd_respons_proponente,
                          nm_respons_concedente, cd_respons_concedente):
        self.responsavel.nm_respons_proponente = nm_respons_proponente
        self.responsavel.cd_respons_proponente = cd_respons_proponente
        self.responsavel.nm_respons_concedente = nm_respons_concedente
        self.responsavel.cd_respons_concedente = cd_respons_concedente

    def build_proposta(self, ano_proposta, nr_proposta, dt_proposta,
                       id_proposta):
        self.proposta.ano_proposta = ano_proposta
        self.proposta.nr_proposta = nr_proposta
        self.proposta.dt_proposta = dt_proposta
        self.proposta.id_proposta = id_proposta

    def build_proponente(self, cd_identif_proponente, nm_proponente,
                         tx_esfera_adm_proponente, tx_regiao_proponente,
                         uf_proponente, nm_municipio_proponente,
                         tx_qualific_proponente, nm_respons_proponente,
                         cd_repons_proponente):
        self.proponente.cd_identif_proponente = cd_identif_proponente
        self.proponente.nm_proponente = nm_proponente
        self.proponente.tx_esfera_adm_proponente = tx_esfera_adm_proponente
        self.proponente.tx_regiao_proponente = tx_regiao_proponente
        self.proponente.uf_proponente = uf_proponente
        self.proponente.nm_municipio_proponente = nm_municipio_proponente
        self.proponente.tx_qualific_proponente = tx_qualific_proponente
        self.proponente.nm_respons_proponente = nm_respons_proponente
        self.proponente.cd_repons_proponente = cd_repons_proponente

    def buid_programa(self, cd_programa, nm_programa, cd_acao_programa):
        self.programa.cd_programa = cd_programa
        self.programa.nm_programa = nm_programa
        self.programa.cd_acao_programa = cd_acao_programa

    def build_datas(self, ano_convenio, dt_inicio_vigencia, dt_fim_vigencia,
                    dt_assinatura, dt_publicacao):
        self.datas.ano_convenio = ano_convenio
        self.datas.dt_inicio_vigencia = dt_inicio_vigencia
        self.datas.dt_fim_vigencia = dt_fim_vigencia
        self.datas.dt_assinatura = dt_assinatura
        self.datas.dt_publicacao = dt_publicacao

    def build_concedente(self, nm_respons_concedente, cd_respons_concedente,
                         nm_orgao_concedente, cd_orgao_concedente):
        self.concedente.nm_respons_concedente = nm_respons_concedente
        self.concedente.cd_respons_concedente = cd_respons_concedente
        self.concedente.nm_orgao_concedente = nm_orgao_concedente
        self.concedente.cd_orgao_concedente = cd_orgao_concedente

    def gerar_servico(self, ano_convenio, nr_convenio, tx_objeto_convenio,
                      id_convenio, tx_modelidade, tx_situacao,
                      tx_substituicao, tx_justificativa, dt_assinatura,
                      dt_publicacao, id_programa, assinado, publicado):
        self.convenio.ano_convenio = ano_convenio
        self.convenio.nr_convenio = nr_convenio
        self.convenio.tx_objeto_convenio = tx_objeto_convenio
        self.convenio.id_convenio = id_convenio
        self.convenio.tx_modelidade = tx_modelidade
        self.convenio.tx_situacao = tx_situacao
        self.convenio.tx_substituicao = tx_substituicao
        self.convenio.tx_justificativa = tx_justificativa
        self.convenio.dt_assinatura = dt_assinatura
        self.convenio.dt_publicacao = dt_publicacao
        self.convenio.id_programa = id_programa
        self.convenio.assinado = assinado
        self.convenio.publicado = publicado
        self.convenio.concedente = self.concedente
        self.convenio.datas = self.datas
        self.convenio.programa = self.programa
        self.convenio.proponente = self.proponente
        self.convenio.proposta = self.proposta
        self.convenio.superior = self.superior
        self.convenio.valores = self.valores
