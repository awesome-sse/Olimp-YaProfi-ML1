import pandas as pd

df = pd.read_csv('train.csv', sep=',')

def change(name):
    global df
    mas = pd.unique(df[name]).tolist()
    df[name] = df[name].map(lambda x: mas.index(x)+1)

print(df.info())
print(df.head())
print(df.describe())

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
df = df[df['Onshore/Offshore']!='ONSHORE-OFFSHORE']
df['Onshore/Offshore'] = df['Onshore/Offshore'].map({'ONSHORE':1,'OFFSHORE':0})

#------------------------------------------------------
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

change('Hydrocarbon type')
change('Reservoir status')
#change('Structural setting')
change('Period')
change('Lithology')

#df['Hydrocarbon type'] = df['Hydrocarbon type']-df['Hydrocarbon type'].mean()
#df['Reservoir status'] = df['Reservoir status']-df['Reservoir status'].mean()
#df['Period'] = df['Period']-df['Period'].mean()
#df['Lithology'] = df['Lithology']-df['Lithology'].mean()

#------------------------------------------------------

tectonic_regime = Counter()

df['Structural setting'] = df['Structural setting'].str.split('/')
df['Structural setting'].map(lambda x: tectonic_regime.update(x))


#print(df1.values)
for i in list(tectonic_regime):
    df[i] = df['Structural setting']
    df[i] = df[i].map(lambda x: 1 if str(x).find(i)!=-1 else 0)

del df['Structural setting']


#------------------------------------------------------
df.to_csv('out.csv', sep=',')
print(df.head())
print(df.describe())
