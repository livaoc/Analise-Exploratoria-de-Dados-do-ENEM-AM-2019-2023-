import pandas as pd

dados_a_coletar = [
    'NU_INSCRICAO',
    'NU_ANO',
    'TP_ESCOLA',
    'SG_UF_PROVA',
    'TP_PRESENCA_LC',
    'TP_PRESENCA_MT',
    'NU_NOTA_CN',
    'NU_NOTA_CH',
    'NU_NOTA_LC',
    'NU_NOTA_MT',
    'NU_NOTA_REDACAO',
    'Q006',
    'Q025',
    'IN_TREINEIRO'
]

anos = [2019, 2020, 2021, 2022, 2023]

for ano in anos:
    df = pd.read_csv(f'raw_data/MICRODADOS_ENEM_{ano}.csv', sep=';', encoding='latin-1', chunksize=100000, usecols=dados_a_coletar)
    novo_arquivo =  f'dados_ENEM_AM_{ano}.csv'
    primeiro_chunk = True

    for chunk in df:
        dados_AM = chunk[(chunk['SG_UF_PROVA'] == 'AM') & (chunk['IN_TREINEIRO']== 0)].copy()
        dados_AM = dados_AM.drop(columns=['IN_TREINEIRO'])

        if primeiro_chunk:
            dados_AM.to_csv(novo_arquivo, index=False, mode='w', encoding='utf-8')
            primeiro_chunk = False
        else:
            dados_AM.to_csv(novo_arquivo, index=False, mode='a', header=False, encoding='utf-8')


print("Coleta finalizada.")
        
