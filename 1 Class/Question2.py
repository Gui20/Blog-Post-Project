import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython import display

df = pd.read_csv('./survey-results-public.csv')


#no_nulls = set(df.columns[df.isnull().mean() == 0])

no_nulls = df.dropna(axis = 1, how = 'any')
no_nulls = set(no_nulls.columns)

print(no_nulls)

