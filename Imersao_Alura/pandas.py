import pandas as pd
#Pandas é uma biblioteca de análise de dados
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv") # ler uma base de dados
print(df.head())
