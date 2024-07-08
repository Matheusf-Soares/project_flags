import pandas as pd

flags = pd.read_csv('flags.csv')

print('head()')
print(flags.head())
print('-' * 90)

print('tail()')
print(flags.tail())
print('-' * 90)

verde = flags['green']
amarelo = flags['gold']
azul = flags['blue']
branco = flags['white']
soma = verde + amarelo + azul + branco

tem_todas = (soma == 4)
tem_todas

print('Países com verde, amarelo, azul e branco')
print(flags[tem_todas.values]['name'])

i = 0
for c in flags.columns:
    i += 1
    att = flags[c]
    att_dtype = att.dtype
    att_tam_dominio = att.unique().size

    att_tem_nulo = any(att.isnull())
    if (att_tam_dominio < 8):
        print(f'({str(i)}) atributo: ', c, '\t', 
              'dtype: ', att_dtype, '\t',
              'nulos: ', att_tem_nulo, '\t',
              'domínio: ', att.unique())
    else:
        if (att_dtype == 'object'):
            print(f'({str(i)}) atributo: ', c, '\t', 
              'dtype: ', att_dtype, '\t',
              'nulos: ', att_tem_nulo, '\t',
              'domínio (primeior elementos): ', att.unique()[:8])
        else:
            print(f'({str(i)}) atributo: ', c, '\t', 
              'dtype: ', att_dtype, '\t',
              'nulos: ', att.min(), '\t',
              'min: ', att.min(), '\t',
              'max: ', att.max(), '\t',
              'media: ', round(att.mean(), 2), '\t',
              'd.p.: ', round(att.std(), 2))
            
df_cores = pd.DataFrame()
for c in flags.columns:
    if c in [ 'red', 'green', 'blue', 'gold', 'white', 'black', 'orange' ]:
        df_cores[c] = flags[c].value_counts()

print(df_cores)

lst_cores = [
    'red',
    'green',
    'blue',
    'gold',
    'white',
    'black',
    'orange',
]

df_cores.plot(kind='barh', # Para criar um gráfico de barras horizontais
              subplots=True, # Para permitir que sejam criados vários gráficos
              figsize=(8, 25), # Define a Altura e Largura do Gráfico
              color=lst_cores) # Define as cores de cada Gráfico

plt.show()