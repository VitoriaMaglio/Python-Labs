import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#Pandas é uma biblioteca de análise de dados
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv") # ler uma base de dados,importar : declara a var, pd.read_csv()
print(df.head()) #mostra as primeiras 5 linhas
#Não estava rodando a biblioteca, e melhorar:
# nome do arquivo não pode ter o mesmo nome da biblioteca que está sendo importada.
# vs tem que usar o mesmo interpretador Python do qual a biblioteca está (verificar a versão da biblioteca e no canto direito da tela, arrumar a versão do py no vs)
#print(df.head(10))
#A indexação sempre começa do zero

#print(df.info())#informações iniciais do arquivo
#print(df.describe())#descrever os dados estatísticamente.

#df.describe é um método ent deve ser chamado com ()
#Ir colocando os comandos como comentários para o arquivo carregar mais rápido.

print(df.shape)
#df.shape é um atributo ent não deve ser colocado com ()
#declarando duas variáveis, pedindo a quant 
linhas, colunas = df.shape[0], df.shape[1]
print('linhas: ' ,linhas, 'colunas: ' , colunas)
 #RESOLVENDO UM PROBLEMA DE NEGOCIOS , ANALISANDO SALARIOS,QUANTIDADE E CARGO DE FUNCIONARIOS ENTENDER RENDIMENTO DA EMPRESA

#print(df.columns)
#ver a frequencia de que cada componente esta na coluna
#print(df["experience_level"].value_counts())

#renomear colunas ; deixar intuitivo as var
#renomear_colunas = {}
#df.rename(columns=renomear_colunas, inplace=True)
novos_nomes = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}
df.rename(columns=novos_nomes, inplace=True)
print(df.head())

#renomear siglas/categorias

senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}
df['senioridade'] = df['senioridade'].replace(senioridade)
df['senioridade'].value_counts()


contrato = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}
df['contrato'] = df['contrato'].replace(contrato)
df['contrato'].value_counts()


tamanho_empresa = {
    'L': 'grande',
    'S': 'pequena',
    'M':	'media'

}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
df['tamanho_empresa'].value_counts()
mapa_trabalho = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}

df['remoto'] = df['remoto'].replace(mapa_trabalho)
df['remoto'].value_counts()
print(df.describe(include='object'))

#reconhecer valores nulos
print(df.isnull().sum())
print(df['ano'].unique())#Checando quais anos existem no DataFrame:
print(df[df.isnull().any(axis=1)])#Exibindo quais linhas estão com os anos nulos:     Sempre começa chamando a base(df) e depois constroi o filtro.


#preencher os dados nulos, excluír eles e 
#criando DATAFRAME
#import numpy as np
#df_salarios = pd.DataFrame({
#    'nome':['Ana','Bruno','Carlos','Diana', 'Eduardo'],
#    'salario' : [4000, np.nan, 3500, np.nan, 5000]
#})
## Preencher com a média salarial ;
## base ['nova coluna'] = dentro desse dataframe, vou pegar a coluna salario , preencher a coluna e com os salarios e a media, e arredondar 
#df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
#
## Preencher com a mediana salarial  reduz um valor muito fora dos outros
#df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
#
#print(df_salarios)
#
#df_temperaturas = pd.DataFrame({
#    'dia': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex'],
#    'temperatura': [30, np.nan, np.nan, 28, 27]
#})
#df_temperaturas['preenchido_ffill'] = df_temperaturas['temperatura'].ffill()
##        nova coluna com os valores  ffil completa com o valor anterior
#print(df_temperaturas)
#    
##preencher com valor fixo
#df_cidades = pd.DataFrame({
#    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
#    'cidade': ['São Paulo', np.nan, 'Curitiba', np.nan, 'Salvador']
#})
#
#df_cidades['cidade_corrigida'] = df_cidades['cidade'].fillna('Não informado')
##                                         preenche com um valor fixo    fillna                
#print(df_cidades)
#
##preenche com um valor posterior bfill
#
#
#df_temperaturas2 = pd.DataFrame({
#    'dia': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex'],
#    'temperatura': [30, np.nan, np.nan, 28, 27]
#})
#
#df_temperaturas2['preenchido_bfill'] = df_temperaturas2['temperatura'].bfill()
#df_temperaturas2

#tratando dados excluindo quando os valores nulos são pequenos perto dos preenchidos
df_limpo = df.dropna()
df_limpo.isnull().sum()#soma os valores nulos

#alterando o tipo de dados
df_limpo.info()# aqui vai trazer as informações dos daados, por exemplo o tipo da coluna ano, que é float, porém ano é um número inteiro ent tem que mudar o tipo
df_limpo = df_limpo.assign(ano=df_limpo['ano'].astype('Int64'))
print(df_limpo.head())

#Aula 03
#Tratando dados de formas visuais com gráficos

#importando dados em gráfico da biblioteca Pandas
#acessar coluna de interesses
# TABELA 1 
#df_limpo['senioridade'].value_counts().plot(kind='bar', title='Distribuição de senioridade')    #calcular frequncias dos dados
#plt.show() #importando a biblioteca de visualização de dados Matplotlib ; serve para criar gráficos, diagramas e visualizações

sns.barplot(data = df_limpo, x='senioridade', y='usd')

#importando a biblioteca de visualização de dados seaborn ; serve para criar gráficos, diagramas e visualizações

plt.figure(figsize=(8,5)) #definindo tamanho da figura 2
sns.barplot(data=df_limpo, x='senioridade', y='usd')
plt.title("Salário médio por senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salário médio anual (USD)")
plt.show()

#ORDENAR maior pro menor valor
#histograma histplot
#boxplot (ou gráfico de caixa) 
#Plotly Express é uma biblioteca de visualização interativa em Python. zoom, hover, ; px como apelido para escrever menos.
#Pycountry é uma biblioteca para lidar com nomes e códigos de países.3
#groupby() + .mean() → agregação de dados.
#value_counts() → contagem de categor
#pycountry → conversão de códigos de p
#px.choropleth() → mapa interativo com cores representando valores.

#Criar ambiente virtual com py(.venv) é uma caixa isolada onde você instala pacotes e bibliotecas só para um projeto em específico, sem misturar com outros projetos no seu pc 
#python -m venv .venv ; .venv\Scripts\Activate