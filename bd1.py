import pandas as pd 
import numpy as np 
df = pd.read_csv("train.csv")

df = pd.get_dummies(df, columns=['Hydrocarbon type',
                                'Reservoir status',
                                 'Period',
                                 'Lithology'])
df = df[df['Onshore/Offshore']!='ONSHORE-OFFSHORE']
df['Onshore/Offshore'] = df['Onshore/Offshore'].map({'ONSHORE':1,'OFFSHORE':0})


sr = (df['Depth'].max()+df['Depth'].min())/2
df['Depth'] = (df['Depth']-sr)**2/sr
sr=(df['Gross'].max()+df['Gross'].min())/2
df['Gross'] = (df['Gross']-sr)**2/sr
sr=(df['Netpay'].max()+df['Netpay'].min())/2
df['Netpay'] = (df['Netpay']-sr)**2/sr
sr=(df['Porosity'].max()+df['Porosity'].min())/2
df['Porosity'] = (df['Porosity']-sr)**2/sr
sr=(df['Permeability'].max()+df['Permeability'].min())/2
df['Permeability'] = (df['Permeability']-sr)**2/sr

#--------------------------------------------------
from collections import Counter
tectonic_regime = Counter()

df['Tectonic regime'] = df['Tectonic regime'].str.split('/')
df['Tectonic regime'].map(lambda x: tectonic_regime.update(x))
print(df.head())
print(tectonic_regime)
print(list(tectonic_regime)[1])

#print(df1.values)
for i in list(tectonic_regime):
    df[i] = df['Tectonic regime']
    df[i] = df[i].map(lambda x: 1 if str(x).find(i)!=-1 else 0)

del df['Tectonic regime']
#------------------------------------------------------

tectonic_regime = Counter()

df['Structural setting'] = df['Structural setting'].str.split('/')
df['Structural setting'].map(lambda x: tectonic_regime.update(x))


#print(df1.values)
for i in list(tectonic_regime):
    df[i] = df['Structural setting']
    df[i] = df[i].map(lambda x: 1 if str(x).find(i)!=-1 else 0)

del df['Structural setting']

#df = df[df['Onshore/Offshore']!='ONSHORE-OFFSHORE']
#df['Onshore/Offshore'] = df['Onshore/Offshore'].map({'ONSHORE':1,'OFFSHORE':0})

print(df.describe())
df.to_csv('out1.csv', sep=',')


#/////////////////////////////////////////////////////////////////////////////////


df1 = pd.read_csv("test.csv")

df1 = pd.get_dummies(df1, columns=['Hydrocarbon type',
                                'Reservoir status',
                                 'Period',
                                 'Lithology'])

#--------------------------------------------------
from collections import Counter
tectonic_regime = Counter()

df1['Tectonic regime'] = df1['Tectonic regime'].str.split('/')
df1['Tectonic regime'].map(lambda x: tectonic_regime.update(x))
print(df1.head())
print(tectonic_regime)
print(list(tectonic_regime)[1])

#print(df1.values)
for i in list(tectonic_regime):
    df1[i] = df1['Tectonic regime']
    df1[i] = df1[i].map(lambda x: 1 if str(x).find(i)!=-1 else 0)

del df1['Tectonic regime']
#------------------------------------------------------

tectonic_regime = Counter()

df1['Structural setting'] = df1['Structural setting'].str.split('/')
df1['Structural setting'].map(lambda x: tectonic_regime.update(x))


#print(df1.values)
for i in list(tectonic_regime):
    df1[i] = df1['Structural setting']
    df1[i] = df1[i].map(lambda x: 1 if str(x).find(i)!=-1 else 0)

del df1['Structural setting']

#df = df[df['Onshore/Offshore']!='ONSHORE-OFFSHORE']
#df['Onshore/Offshore'] = df['Onshore/Offshore'].map({'ONSHORE':1,'OFFSHORE':0})

for i in list(df):
    if (i not in list(df1)) and i!='Onshore/Offshore':
        df1[i] = 0

for i in list(df1):
    if i not in list(df):
        del df1[i]

print(df1.describe())
df1.to_csv('out_test.csv', sep=',')
