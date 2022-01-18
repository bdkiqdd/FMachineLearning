# Project Two - Predict of finance return on Public Investment

# Imports

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.formats import style
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score
import warnings
warnings.filterwarnings("ignore")

# Data load

df = pd.read_csv("dados/dataset.csv")
print("\nCarregando dados")
print("\nDados carregados com sucesso")
print(f"Shape {df.shape}")
print(df.head)

# Data Viz

df.plot(x = 'Investimento',y= 'Retorno',style= 'o')
plt.title('Investimento x Retorno')
plt.xlabel('Investimento')
plt.ylabel('Retorno')
plt.savefig('images/first-graf.png')
plt.show()

# Data preparation

x = df.iloc[:,:-1].values
y = df.iloc[:,1].values

