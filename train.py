import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Loaded data
df=pd.read_csv('Dataset/Algerian_forest_fires_dataset.csv')
print(df.head())
# information of dataset
print(df.info())

#Data cleaning
##missing values
print(df.isnull().any(axis=1))

#The dataset is converted into two sets based on region from 122th index, we can make a new column based on the region.
# 1. "Bejaia Region Dataset"
# 2. "Sidi-Bel Abbes Region Dataset"
df.loc[:125,"Region"]=0
df.loc[128:,"Region"]=1
print(df.info())