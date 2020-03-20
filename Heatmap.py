import pandas as pd 
import matplotlib as plt
from matplotlib import figure
import seaborn as sns
import numpy as np 

#%matplotlib inline

df = pd.read_csv('avocado.csv')
df.columns 
df.head()
df.dtypes
f = figure.Figure(figsize=(10,5))
sns.heatmap(df.corr(), annot= True, linewidth=0.5, cmap='Blues')
