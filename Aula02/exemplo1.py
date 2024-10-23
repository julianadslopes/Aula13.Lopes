import os
import pandas as pd
import numpy as np

os.system ("cls")

# média = (2000+2500+3000+3500+4000+30000)/6
# print(média)

dados_salario = [2000, 2500, 3000, 3500, 4000, 30000]
media = np.mean(dados_salario)
print ("Média: ", media)

mediana = np.median (dados_salario)
print ("Mediana: ", mediana)