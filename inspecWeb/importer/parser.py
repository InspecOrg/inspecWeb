#! /usr/bin/env python
import pandas as pd
# from django.core.exceptions import ObjectDoesNotExist
import importer.csv_parser as csv_p
from authentication.models import InspecUser
from core.models import Convenio


class Importer(object):

    def import_data(self):
        csv_p.parse_all()
        self.import_convenios()

    def read_file(self, file_name):
        try:
            data = pd.read_csv(file_name, ';', header=0)
        except (IOError, NameError):
            print ('Erro ao ler o arquivo' + file_name + ', verifique\
se ele se encontra no mesmo diretorio que parser.py')
        return data

    def import_convenios(self):
        data = self.read_file('convenio.csv')

        print('Inporting Convenios')

        for index, row in data.iterrows():
            convenio = Convenio()
            convenio.ano_convenio = row['ANO_CONVENIO']
            convenio.nr_convenio = row['NR_CONVENIO']
            convenio.tx_objeto_convenio = row['TX_OBJETO_CONVENIO']
            convenio.id_convenio = row['ID_CONVENIO']
            convenio.tx_modelidade = row['TX_MODALIDADE']
            convenio.tx_situacao = row['TX_SITUACAO']
            convenio.tx_substituicao = row['TX_SUBSITUACAO']
            convenio.tx_justificativa = row['TX_JUSTIFICATIVA']
            convenio.dt_assinatura = row['DT_ASSINATURA']
            convenio.dt_publicacao = row['DT_PUBLICACAO']
            convenio.id_programa = row['ID_PROP_PROGRAMA']
            convenio.assinado = row['ASSINADO']
            convenio.publicado = row['PUBLICADO']
            convenio.save()


if __name__ == "__main__":
    importer = Importer()
    importer.import_data()
