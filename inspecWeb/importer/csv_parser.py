#! /usr/bin/env python

import sys
import argparse
import pandas as pd

parser = argparse.ArgumentParser(
    description='Parser para dados livres de convenios')

parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                    default=False)

options = parser.parse_args(sys.argv[1:])

try:
    data = pd.read_csv('05_PropostasPrograma.csv', ';', header=0)
except (IOError, NameError):
    print ('Erro ao ler o arquivo 05_PropostasPrograma.csv, verifique se ele\
se encontra no mesmo diretorio que parser.py')


def parse(headers, csv_name):
    saida = data[headers]
    saida.to_csv(csv_name, sep=';', index=False)
    if options.verbose:
        print(saida.head(5))


def parse_proposta():
    parse(['ANO_PROPOSTA', 'NR_PROPOSTA', 'DT_PROPOSTA',
           'ID_PROPOSTA'], 'proposta.csv')


def parse_convenio():
    convenio = data[['ANO_CONVENIO', 'NR_CONVENIO', 'TX_OBJETO_CONVENIO',
                     'ID_CONVENIO', 'TX_MODALIDADE', 'TX_SITUACAO',
                     'TX_SUBSITUACAO', 'TX_JUSTIFICATIVA', 'DT_ASSINATURA',
                     'DT_PUBLICACAO', 'ID_PROP_PROGRAMA']]
    convenio["ASSINADO"] = convenio["DT_ASSINATURA"].isnull().map(
        lambda x: False if x is True else True)
    convenio["PUBLICADO"] = convenio["DT_PUBLICACAO"].isnull().map(
        lambda x: False if x is True else True)
    convenio.to_csv('convenio.csv', sep=';', index=False)
    if options.verbose:
        print (convenio.head(5))


def parse_datas():
    parse(['ANO_CONVENIO', 'DT_INICIO_VIGENCIA', 'DT_FIM_VIGENCIA',
           'DT_ASSINATURA', 'DT_PUBLICACAO'], 'datas.csv')


def parse_proponente():
    parse(['CD_IDENTIF_PROPONENTE', 'NM_PROPONENTE',
           'TX_ESFERA_ADM_PROPONENTE', 'TX_REGIAO_PROPONENTE',
           'UF_PROPONENTE', 'NM_MUNICIPIO_PROPONENTE',
           'TX_QUALIFIC_PROPONENTE', 'NM_RESPONS_PROPONENTE',
           'CD_RESPONS_PROPONENTE'], 'proponente.csv')


def parse_responsavel():
    parse(['NM_RESPONS_PROPONENTE', 'CD_RESPONS_PROPONENTE',
           'NM_RESPONS_CONCEDENTE', 'CD_RESPONS_CONCEDENTE'], 'responsavel.csv')


def parse_valores():
    parse(['VL_GLOBAL', 'VL_REPASSE', 'VL_REPASSE_EXERC_ATUAL',
           'VL_CONTRAPARTIDA', 'VL_CONTRAPARTIDA_FINANC',
           'VL_CONTRAPARTIDA_BENS_SERV'], 'valores.csv')


def parse_concedente():
    parse(['NM_RESPONS_CONCEDENTE', 'CD_RESPONS_CONCEDENTE',
           'NM_ORGAO_CONCEDENTE', 'CD_ORGAO_CONCEDENTE'], 'concedente.csv')


def parse_superior():
    parse(['NM_ORGAO_SUPERIOR',  'CD_ORGAO_SUPERIOR'], 'superior.csv')


def parse_programa():
    parse(['CD_PROGRAMA', 'NM_PROGRAMA', 'CD_ACAO_PROGRAMA'], 'programa.csv')


def parse_all():
    parse_proposta()
    parse_convenio()
    parse_datas()
    parse_proponente()
    parse_responsavel()
    parse_valores()
    parse_concedente()
    parse_superior()
    parse_programa()

if __name__ == "__main__":
    parse_proposta()
    parse_convenio()
    parse_datas()
    parse_proponente()
    parse_responsavel()
    parse_valores()
    parse_concedente()
    parse_superior()
    parse_programa()
