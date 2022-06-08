import pandas as pd
from datetime import date
import json


class CnabParser:
    def __init__(self):
        data_full = date.today().isoformat()
        d_info = data_full.split('-')
        data_formatted = f"{d_info[2]}{d_info[1]}{d_info[0]}"
        self.title = f"CB{d_info[2]}{d_info[1]}C66"
        self.date_now = data_formatted
        self.var2 = 'test_variable'

        with open('//home/adriano/dev/projects/cnab/fdic_06-06.csv', 'r', encoding='ISO-8859-1') as file:
            self.sheet = pd.read_csv(file, header=0, sep=';')
            self.df = pd.DataFrame(self.sheet)
            self.df_selected_items = pd.DataFrame()
            self.json_cnab = []
            for row in self.df.iterrows():
                if row[1][7] == 'KAIIMA BRASIL SEMENTES LTDA.':
                    self.json_cnab.append(pd.DataFrame.to_json(row[1]))

    def ulend_data(self, input_data: dict) -> list:
        ulend_data = []

        item3_1a3_5 = f"08REMESSA01       "
        ulend_data.append(item3_1a3_5)

        item3_6a3_11cod_originador = f"00000037069604000102   " \
                                     f"ULEND GESTAO DE ATIVOS LTDA341BANCO ITAU S.A.{self.date_now}{8*' '}"
        ulend_data.append(item3_6a3_11cod_originador)

        item3_13 = input_data['NU_DOCUMENTO']
        ulend_data.append(item3_13)

        item3_12a3_15 = f"MX{item3_13}{377*' '}000001"  # REVER DADOS APOS MX
        ulend_data.append(item3_12a3_15)

        return ulend_data

    def fdic_data(self, input_data: dict) -> list:
        fdic_data = []

        nome = input_data['NOME_SACADO']    # iterar
        fdic_data.append(nome)
        # endereco = input_data['ENDERECO']   # check source for this information
        # cep = input_data['CEP']   # check source for this information
        cnpj = input_data['DOC_SACADO']
        format_cnpj_string = {".": "", "/": "", "-": ""}
        for key, value in format_cnpj_string.items():
            cnpj = cnpj.replace(key, value)  # check algorithm to format cnpj data (only integers)
        fdic_data.append(cnpj)

        item3_13 = input_data['NU_DOCUMENTO']
        fdic_data.append(item3_13)

        item4_1a4_4 = "10000001"  # identificação = 1 ; data da carencia = 000000 ; tipo de juros = 1 - fixo
        item4_17 = input_data['VALOR_NOMINAL']
        item4_5a4_20 = f"{0*10}02990215010199 B0             {item3_13}_070000000000000000000 {item4_17}  {self.date_now}{8*' '}"

        item4_24 = input_data['VALOR_NOMINAL']
        item4_21a4_26 = f"15 {item3_13}{self.date_now}{7*0}{item4_24}{8*0}41"

        item4_27a4_33 = f" {self.date_now}00002{12*0}{19*' '}"

        item4_34 = input_data['VALOR_AQUISICAO']
        item4_34a4_41 = f"{7*0}{item4_34}{13*0}02{cnpj}{nome}<check endereço>{12*0}"

        seq_registro = input_data['SEU_NUMERO']  # valor apos o underline
        item4_42 = f"Ulend Gestao Financeira Ltda.32475607000114{100*0}{seq_registro}"
        # juros_mensal + juros_mora + multa + 71zeros

        item5_1a5_3 = f"9{493*' '}{seq_registro}"

        item4_34 = '444,00'
        t2 = self.var2
        return fdic_data

    # def selected_table_data(self):
    #     for item in self.json_cnab:


if __name__ == '__main__':
    print('CNAB PARSER\n')
    cnab = CnabParser()
    # teste = cnab.ulend_data()
    teste1 = cnab.date_now
    # teste2 = cnab.fdic_data()
    # print(teste, ' - ', teste1, ' - ', teste2)
    # print(teste[1])
    # print(cnab.table)
    # print(cnab.df_selected_items)
    # print(type(cnab.json_cnab))
    # print(cnab.json_cnab)

    cnab_volume = cnab.json_cnab

    # for cnab_data in cnab_volume:
    #     print(cnab.ulend_data(cnab_data))

    for series in cnab_volume:
        series = json.loads(series)
        print(type(series))
        teste5 = cnab.ulend_data(series)
        print(teste5)
        teste6 = cnab.fdic_data(series)
        print(teste6)
