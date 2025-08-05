import pandas as pd
#Pandas é uma biblioteca de análise de dados
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv") # ler uma base de dados
print(df.head())
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