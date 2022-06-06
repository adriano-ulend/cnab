import pandas as pd
from datetime import date


class CnabParser:
    def __init__(self):
        data_full = date.today().isoformat()
        d_info = data_full.split('-')
        data_formatted = f"{d_info[2]}{d_info[1]}{d_info[0]}"
        self.title = f"CB{d_info[2]}{d_info[1]}C66"
        self.date_now = data_formatted

        with open('//home/adriano/dev/projects/cnab/Estoque_FIDC ULEND_001.csv', 'r', encoding='ISO-8859-1') as file:
            self.sheet = pd.read_csv(file, header=0, sep=';')
            self.df = pd.DataFrame(self.sheet)
            self.var2 = 0
            for row in self.df.iterrows():
                if self.df.loc[self.df['NOME_CEDENTE']] == 'KAIIMA BRASIL SEMENTES LTDA.':
                    self.var2 = 2
                    break

    def ulend_data(self):
        item3_1a3_5 = f"08REMESSA01       "
        table = self.df
        return item3_1a3_5, table

    def fdic_data(self):
        item4_34 = '444,00'
        t2 = self.var2
        return item4_34, t2


if __name__ == '__main__':
    print('CNAB PARSER\n')
    cnab = CnabParser()
    teste = cnab.ulend_data()
    teste1 = cnab.date_now
    teste2 = cnab.fdic_data()
    # print(teste, ' - ', teste1, ' - ', teste2)
    # print(teste[1])
    # print(cnab.table)
