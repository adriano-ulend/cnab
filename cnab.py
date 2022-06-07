import pandas as pd
from datetime import date


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
                    # self.df_selected_items = self.df_selected_items.append(row[1])
                    self.json_cnab.append(pd.DataFrame.to_json(row[1]))

    def ulend_data(self, input_data):
        data = []

        item3_1a3_5 = f"08REMESSA01       "
        data.append(item3_1a3_5)
        item3_6a3_11cod_originador = f"00000037069604000102   ULEND GESTAO DE ATIVOS LTDA341BANCO ITAU S.A.{self.date_now}{8*' '}"
        data.append(item3_6a3_11cod_originador)

        return data

    def fdic_data(self):
        item4_34 = '444,00'
        t2 = self.var2
        return item4_34, t2

    # def selected_table_data(self):
    #     for item in self.json_cnab:


if __name__ == '__main__':
    print('CNAB PARSER\n')
    cnab = CnabParser()
    # teste = cnab.ulend_data()
    teste1 = cnab.date_now
    teste2 = cnab.fdic_data()
    # print(teste, ' - ', teste1, ' - ', teste2)
    # print(teste[1])
    # print(cnab.table)
    # print(cnab.df_selected_items)
    # print(type(cnab.json_cnab))
    # print(cnab.json_cnab)

    cnab_volume = cnab.json_cnab

    for cnab_data in cnab_volume:
        print(cnab.ulend_data(cnab_data))
