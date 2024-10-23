import numpy as np
import pandas as pd
import os

os.system("cls")

df = pd.read_excel("vendas_roupas1.xlsx")
print (df)
print (30* "=")

categoria = df["Categoria"]
quantidade_vendida = df ["Quantidade Vendida"]
print (quantidade_vendida.describe)
print (categoria)
print (30* "=")

q1 = np.quantile(quantidade_vendida,0.25)
q2 = np.quantile(quantidade_vendida,0.5)
q3 = np.quantile(quantidade_vendida,0.75)
print (f" Q1 25% : {q1}")
print (f" Q2 50% : {q2}")
print (f" Q3 75% : {q3}") 
print (30* "=")

media = np.mean(quantidade_vendida)
mediana = np.median(quantidade_vendida)

print (f"Média: {media}")
print (f"Mediana: {mediana}")
print (30* "=")

print ("USANDO DESCRIBE")
print (quantidade_vendida.describe())
print (30* "=")
print ("USANDO DESCRIBE")
print (categoria.describe())
print (30* "=")

print ("USANDO UNIQUE")
print (quantidade_vendida.unique())
print (30* "=")
print ("USANDO UNIQUE")
print (categoria.unique())
print (30* "=")

quantidade_vendida_ord = df.sort_values(by= "Quantidade Vendida", ascending = True)
quantidade_vendida = quantidade_vendida_ord["Quantidade Vendida"]
print (quantidade_vendida.values)