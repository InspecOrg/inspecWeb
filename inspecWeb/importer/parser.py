#! /usr/bin/env python
import pandas as pd
# from django.core.exceptions import ObjectDoesNotExist
# import importer.csv_parser as csv_p
# from authentication.models import InspecUser
from core.models import (Convenio, Concedente, Datas, Programa, Proponente,
                         Proposta, Superior, Valores, ConvenioBuilder)
from datetime import datetime
from re import sub
from abc import abstractmethod


class Importer(object):

    def import_data(self, qnt_conv):
        self.import_servico(qnt_conv)

    @abstractmethod
    def read_file(self, file_name, nrows):
        raise NotImplementedError()

    @abstractmethod
    def import_convenios(self, qnt_conv):
        raise NotImplementedError()


class ConvImporter(Importer):

    convenio_builder = ConvenioBuilder()

    def import_data(self, qnt_conv):
        self.import_convenios(qnt_conv)

    def read_file(self, file_name, nrows):
        try:
            data = pd.read_csv(file_name, ';', header=0, nrows=nrows)
        except (IOError, NameError):
            print ('Erro ao ler o arquivo' + file_name + ', verifique\
se ele se encontra no mesmo diretorio que parser.py')
        return data

    def import_convenios(self, qnt_conv):
        conv_data = self.read_file('importer/convenio.csv', qnt_conv)
        conc_data = self.read_file('importer/concedente.csv', qnt_conv)
        datas_data = self.read_file('importer/datas.csv', qnt_conv)
        programa_data = self.read_file('importer/programa.csv', qnt_conv)
        propon_data = self.read_file('importer/proponente.csv', qnt_conv)
        proposta_data = self.read_file('importer/proposta.csv', qnt_conv)
        resp_data = self.read_file('importer/responsavel.csv', qnt_conv)
        sup_data = self.read_file('importer/superior.csv', qnt_conv)
        val_data = self.read_file('importer/valores.csv', qnt_conv)

        print('Inporting Convenios')

        # for index, row in zip(conv_data.iterrows(), conc_data.iterrows(),
        #                       datas_data.iterrows(), programa_data.iterrows(),
        #                       propon_data.iterrows(), proposta_data.iterrows(),
        #                       resp_data.iterrows(), sup_data.iterrows(),
        #                       val_data.iterrows()):
        for index, row in conv_data.iterrows():
            # concedente
            nm_respons_concedente = conc_data['NM_RESPONS_CONCEDENTE'][index]
            cd_respons_concedente = conc_data['CD_RESPONS_CONCEDENTE'][index]
            nm_orgao_concedente = conc_data['NM_ORGAO_CONCEDENTE'][index]
            cd_orgao_concedente = conc_data['CD_ORGAO_CONCEDENTE'][index]
            self.convenio_builder.build_concedente(nm_respons_concedente,
                                                   cd_respons_concedente,
                                                   nm_orgao_concedente,
                                                   cd_orgao_concedente)
            # datas
            try:
                ano_convenio = datetime.strptime(
                    str(datas_data['ANO_CONVENIO'][index]), '%Y'
                )
            except:
                ano_convenio = None
            dt_inicio_vigencia = datetime.strptime(
                datas_data['DT_INICIO_VIGENCIA'][index], '%d/%m/%Y'
            )
            dt_fim_vigencia = datetime.strptime(
                datas_data['DT_FIM_VIGENCIA'][index], '%d/%m/%Y'
            )
            try:
                dt_assinatura = datetime.strptime(
                    datas_data['DT_ASSINATURA'][index], '%d/%m/%Y'
                )
            except:
                dt_assinatura = None
            try:
                dt_publicacao = datetime.strptime(
                    datas_data['DT_PUBLICACAO'][index], '%d/%m/%Y'
                )
            except:
                dt_publicacao = None
            self.convenio_builder.build_datas(ano_convenio,
                                              dt_inicio_vigencia,
                                              dt_fim_vigencia,
                                              dt_assinatura,
                                              dt_publicacao)

            # programa
            cd_programa = programa_data['CD_PROGRAMA'][index]
            nm_programa = programa_data['NM_PROGRAMA'][index]
            cd_acao_programa = programa_data['CD_ACAO_PROGRAMA'][index]
            self.convenio_builder.buid_programa(cd_programa,
                                                nm_programa,
                                                cd_acao_programa)

            # proponente
            cd_identif_proponente = propon_data['CD_IDENTIF_PROPONENTE'][index]
            nm_proponente = propon_data['NM_PROPONENTE'][index]
            tx_esfera_adm_proponente = str(
                propon_data['TX_ESFERA_ADM_PROPONENTE'][index]
            )
            tx_regiao_proponente = propon_data['TX_REGIAO_PROPONENTE'][index]
            uf_proponente = propon_data['UF_PROPONENTE'][index]
            nm_municipio_proponente = str(
                propon_data['NM_MUNICIPIO_PROPONENTE'][index]
            )
            tx_qualific_proponente = str(
                propon_data['TX_QUALIFIC_PROPONENTE'][index]
            )
            nm_respons_proponente = propon_data['NM_RESPONS_PROPONENTE'][index]
            try:
                cd_repons_proponente = float(
                    propon_data['CD_REPONS_PROPONENTE'][index]
                )
            except:
                cd_repons_proponente = None
            self.convenio_builder.build_proponente(cd_identif_proponente,
                                                   nm_proponente,
                                                   tx_esfera_adm_proponente,
                                                   tx_regiao_proponente,
                                                   uf_proponente,
                                                   nm_municipio_proponente,
                                                   tx_qualific_proponente,
                                                   nm_respons_proponente,
                                                   cd_repons_proponente)

            # proposta
            ano_proposta = datetime.strptime(
                str(proposta_data['ANO_PROPOSTA'][index]), '%Y'
            )
            nr_proposta = int(proposta_data['NR_PROPOSTA'][index])
            dt_proposta = datetime.strptime(
                proposta_data['DT_PROPOSTA'][index], '%d/%m/%Y'
            )
            id_proposta = proposta_data['ID_PROPOSTA'][index]
            self.convenio_builder.build_proposta(ano_proposta,
                                                 nr_proposta,
                                                 dt_proposta,
                                                 id_proposta)

            # responsavel
            nm_respons_proponente = resp_data['NM_RESPONS_PROPONENTE'][index]
            cd_respons_proponente = float(
                resp_data['CD_RESPONS_PROPONENTE'][index]
            )
            nm_respons_concedente = resp_data['NM_RESPONS_CONCEDENTE'][index]
            try:
                cd_respons_concedente = float(
                    resp_data['CD_RESPONS_CONCEDENTE'][index]
                )
            except:
                cd_respons_concedente = None
            self.convenio_builder.build_responsavel(nm_respons_proponente,
                                                    cd_respons_proponente,
                                                    nm_respons_concedente,
                                                    cd_respons_concedente)
            # superior
            nm_orgao_superior = sup_data['NM_ORGAO_SUPERIOR'][index]
            cd_orgao_superior = sup_data['CD_ORGAO_SUPERIOR'][index]
            self.convenio_builder.build_superior(nm_orgao_superior,
                                                 cd_orgao_superior)

            # valores
            vl_global = self.money_to_int(val_data['VL_GLOBAL'][index])
            vl_repasse = self.money_to_int(val_data['VL_REPASSE'][index])
            vl_repasse_exerc_atual = self.money_to_int(
                val_data['VL_REPASSE_EXERC_ATUAL'][index]
            )
            vl_contrapartida = self.money_to_int(
                val_data['VL_CONTRAPARTIDA'][index]
            )
            vl_contrapartida_financ = self.money_to_int(
                val_data['VL_CONTRAPARTIDA_FINANC'][index]
            )
            vl_contrapartida_bens_serv = self.money_to_int(
                val_data['VL_CONTRAPARTIDA_BENS_SERV'][index]
            )
            self.convenio_builder.build_valores(vl_global,
                                                vl_repasse,
                                                vl_repasse_exerc_atual,
                                                vl_contrapartida,
                                                vl_contrapartida_financ,
                                                vl_contrapartida_bens_serv)

            # servico, convenio
            try:
                ano_convenio = datetime.strptime(
                    str(row['ANO_CONVENIO']), '%Y'
                )
            except:
                ano_convenio = None
            try:
                nr_convenio = int(row['NR_CONVENIO'])
            except:
                nr_convenio = None
            tx_objeto_convenio = row['TX_OBJETO_CONVENIO']
            try:
                id_convenio = int(row['ID_CONVENIO'])
            except:
                id_convenio = None
            tx_modelidade = row['TX_MODALIDADE']
            tx_situacao = row['TX_SITUACAO']
            tx_substituicao = row['TX_SUBSITUACAO']
            tx_justificativa = row['TX_JUSTIFICATIVA']
            assinado = row['ASSINADO']
            publicado = row['PUBLICADO']
            if assinado:
                dt_assinatura = datetime.strptime(
                    str(row['DT_ASSINATURA']), "%d/%m/%Y"
                )
            else:
                dt_assinatura = None
            if publicado:
                dt_publicacao = datetime.strptime(
                    str(row['DT_PUBLICACAO']), "%d/%m/%Y"
                )
            else:
                dt_publicacao = None
            id_programa = row['ID_PROP_PROGRAMA']
            convenio = self.convenio_builder.gerar_servico(ano_convenio,
                                                           nr_convenio,
                                                           tx_objeto_convenio,
                                                           id_convenio,
                                                           tx_modelidade,
                                                           tx_situacao,
                                                           tx_substituicao,
                                                           tx_justificativa,
                                                           dt_assinatura,
                                                           dt_publicacao,
                                                           id_programa,
                                                           assinado,
                                                           publicado)
            convenio.save()

    def str_to_bool(self, s):
        if s == 'True':
            return True
        elif s == 'False':
            return False

    def money_to_int(self, money):
        money = money[:-3]
        money = sub(r'[^\d.]', '', money)
        money = money.replace('.', '')
        return int(money)

if __name__ == "__main__":
    importer = Importer()
    importer.import_data()
