import os
import pandas as pd
import numpy as np

os.system ("cls")

df = pd.read_excel("vendas_eletos_eletronicos2.xlsx")
print (df.head())
print (30* "=")

# MEDIDAS DE TENDÊNCIA CENTRAL
print ("Medidas de tendência central do valor total")
media = np.mean (df["Total"])
mediana = np.median (df["Total"])
print (f"Média: {media} ")
print (f"Mediana: {mediana} ")
print (30* "=")

# DETERMINANDO OS QUARTIS
q1 = np.quantile(df["Total"], 0.25)
q2 = np.quantile(df["Total"], 0.50)
q3 = np.quantile(df["Total"], 0.75)
print ("QUARTIS")
print (f"Q1: {q1}")
print (f"Q2: {q2}")
print (f"Q3: {q3}")
print (30* "=")

# Identificar os produtos que estão entre os mais vendidos
mais_vendidos = df.sort_values(by= "Total", ascending = False)
print (mais_vendidos.head())
print (30* "=")

# Identificando os produtos que estão entre os menos vendidos
menos_vendidos = df.sort_values(by= "Total", ascending = True)
print (menos_vendidos.head())
print (30* "=")

# Apresentação dos Resultados
print ("Os dados observados mostram que, entre a média e a mediana, a mediana representa melhor os valores totais das vendas, \n tendo em vista alguns valores discrepantes que influenciam na média.")
print (" Os quartis calculados mostram que 25% dos valores observados estão abaixo de 10960, enquanto outros 25% estão acima de 49746.75.")
print (" Os itens mais vendidos foram: Notebook, Smartphone, Smart TV, Ar condicionado e geladeira. \n Já os menos vendidos foram: ferro de passar, cafeteira, fone de ouvido, liquidificador e torradeira.")