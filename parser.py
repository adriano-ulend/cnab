import json

import pandas as pd
from datetime import date

def cnab():
    with open('//home/adriano/dev/projects/cnab/fdic_06-06.csv', 'r', encoding='ISO-8859-1') as file:

        sheet = pd.read_csv(file, header=0, sep=';')
        df = pd.DataFrame(sheet)
        df2 = pd
        df_selected = []
        list_selected = []

        for e, row in enumerate(df.iterrows()):
            if row[1][7] =='KAIIMA BRASIL SEMENTES LTDA.':
                df_selected.append(pd.DataFrame.to_json(row[1]))

        # print(df_selected)
        for item in df_selected:
            dict_item = json.loads(item)
            print(type(dict_item))

        # return df2

        # df['VALIDATION'] = 'NA'
        # # print(df)
        # #
        # # for i, c in df.iterrows():
        # #     if c['SITUACAO_RECEBIVEL'] == 'Vencido':
        # #         df.loc[i, 'VALIDATION'] = 'check'
        # #     else:
        # #         df.loc[i, 'VALIDATION'] = 'aberto'
        # #
        # # print(df)
        #
        # nome = df['NOME_SACADO']    # iterar
        # endereco = df['ENDERECO']   # iterar e buscar dado do sacado
        # cep = df['CEP']
        # cnpj = df['DOC_SACADO']
        # for i, cnpj_data in cnpj.iteritems():
        #     cnpj_full = cnpj_data.replace([".", "/", "-"], "")  # check algorithm to format cnpj data (only integers)
        #
        # data_full = date.today().isoformat()
        # d_info = data_full.split('-')
        # data_formatted = f"{d_info[2]}{d_info[1]}{d_info[0]}"
        # title = f"CB{d_info[2]}{d_info[1]}C66"
        #
        # item3_1a3_5 = f"08REMESSA01       "
        #
        # item3_6a3_11cod_originador = f"00000037069604000102   ULEND GESTAO DE ATIVOS LTDA341BANCO ITAU S.A.{data_formatted}{8*' '}"
        #
        # item3_13 = df['NU_DOCUMENTO'][0]
        # item3_12a3_15 = f"MX{item3_13}{377*' '}000001"  # REVER DADOS APOS MX
        #
        # item4_1a4_4 = "10000001"  # identificação = 1 ; data da carencia = 000000 ; tipo de juros = 1 - fixo
        # item4_17 = df['VALOR_NOMINAL']
        # item4_5a4_20 = f"{0*10}02990215010199 B0             {item3_13}_070000000000000000000 {item4_17}  {data_formatted}{8*' '}"
        #
        # item4_24 = df['VALOR_NOMINAL'][0]
        # item4_21a4_26 = f"15 {item3_13}{data_formatted}{7*0}{item4_24}{8*0}41"
        #
        # item4_27a4_33 = f" {data_formatted}00002{12*0}{19*' '}"
        #
        # item4_34 = df['VALOR_AQUISICAO']
        # item4_34a4_41 = f"{7*0}{item4_34}{13*0}02{cnpj_full}{nome}{endereco}{12*0}"
        #
        # seq_registro = df['SEU_NUMERO'][1]  # valor apos o underline
        # item4_42 = f"Ulend Gestao Financeira Ltda.32475607000114{100*0}{seq_registro}"
        # # juros_mensal + juros_mora + multa + 71zeros
        #
        # item5_1a5_3 = f"9{493*' '}{seq_registro}"
        #
        # print('check')
        # return title



if __name__ == '__main__':
    print(cnab())

# TO-DO:
# OK 1. Puxar row de acordo com condicional/filtro de valores de determinada coluna
# OK 2. Adicionar linhas selecionadas a um novo dataframe (replace por uma lista com json - salvar no mongo)
# ok 3. A partir do novo dataframe extrair dados para o cnab (fdic_data)
# 4. verificar retorno das defs da classe para ser inserida no cnab (def main() antes do if)
# 5. check no doc final do cnab (documento em .txt)
