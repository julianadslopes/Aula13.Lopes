import numpy as np
import os
os.system("cls")

dados = np.array ([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])
print (dados)

q1 = np.quantile (dados, 0.25)
q2 = np.quantile (dados, 0.5)
q3 = np.quantile (dados, 0.75)
print (f" Q1 25% : {q1}")
print (f" Q2 50% : {q2}")
print (f" Q3 75% : {q3}") 