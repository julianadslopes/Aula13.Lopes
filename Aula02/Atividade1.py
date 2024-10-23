import os
import pandas as pd
import numpy as np

os.system("cls")

casas = [150000, 180000, 200000, 220000, 250000, 280000, 300000, 320000, 400000, 1500000]

media = np.mean(casas)
print (f"A média dos valores das casas é de R$ {media:.2f}")

mediana = np.median(casas)
print (f"O valor mediano das casas é R$ {mediana:.2f} ")

print ("O valor da mediana representa melhor o valor típico das casas pois está mais próximo da maioria dos valores de venda")