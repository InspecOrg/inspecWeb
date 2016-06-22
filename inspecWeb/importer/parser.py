#! /usr/bin/env python
import pandas as pd
# from django.core.exceptions import ObjectDoesNotExist
# import importer.csv_parser as csv_p
# from authentication.models import InspecUser
from core.models import Convenio
from datetime import datetime


class Importer(object):

    def import_data(self):
        self.import_convenios()

    def read_file(self, file_name):
        try:
            data = pd.read_csv(file_name, ';', header=0)
        except (IOError, NameError):
            print ('Erro ao ler o arquivo' + file_name + ', verifique\
se ele se encontra no mesmo diretorio que parser.py')
        return data

    def import_convenios(self):
        data = self.read_file('importer/convenio.csv')

        print('Inporting Convenios')

        for index, row in data.iterrows():
            convenio = Convenio()
            try:
                convenio.ano_convenio = datetime.strptime(row['ANO_CONVENIO'])
            except:
                convenio.ano_convenio = None
            # convenio.nr_convenio = int(row['NR_CONVENIO'])
            convenio.tx_objeto_convenio = row['TX_OBJETO_CONVENIO']
            # convenio.id_convenio = int(row['ID_CONVENIO'])
            convenio.tx_modelidade = row['TX_MODALIDADE']
            convenio.tx_situacao = row['TX_SITUACAO']
            convenio.tx_substituicao = row['TX_SUBSITUACAO']
            convenio.tx_justificativa = row['TX_JUSTIFICATIVA']
            convenio.assinado = row['ASSINADO']
            convenio.publicado = row['PUBLICADO']
            if convenio.assinado:
                convenio.dt_assinatura = datetime.strptime(
                    str(row['DT_ASSINATURA']), "%d/%m/%Y"
                )
            else:
                convenio.dt_assinatura = None
            if convenio.publicado:
                convenio.dt_publicacao = datetime.strptime(
                    str(row['DT_PUBLICACAO']), "%d/%m/%Y"
                )
            else:
                convenio.dt_publicacao = None
            convenio.id_programa = row['ID_PROP_PROGRAMA']
            convenio.save()

    def str_to_bool(self, s):
        if s == 'True':
            return True
        elif s == 'False':
            return False

if __name__ == "__main__":
    importer = Importer()
    importer.import_data()
