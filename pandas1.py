import pandas as pd 
import numpy as np 
df = pd.DataFrame(np.arange(0,20).reshape(4,5),index=['R1','R2','R3','R4'],columns=['C1','C2','C3','C4','C5'])
print(df.head())
#df.to_csv('test1.csv')

#accessing the elemnts

print(df.loc['R1'])

print(type(df.loc['R1']))

print(df.iloc[0:3,0:2])

print(type(df.iloc[0:3,0:2]))

print(type(df.iloc[0:1,0:1]))

print(df.iloc[0:1,0:1])

print(df.iloc[:,:].values)

print(df.iloc[:,:].values.shape)

print(df.isnull().sum())

print(df['C1'].unique())

print(df['C1'].value_counts())

print(df[['C1','C2','C4']])
