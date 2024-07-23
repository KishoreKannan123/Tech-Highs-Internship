import pandas as pd
import numpy as np
from numpy import linalg as LA

df = pd.read_csv('colors.csv',header=None)
df.drop(columns=[0,2],inplace=True)
df.columns = ['Color','R','G','B']
df['Target'] = df.index

def colour(vec):
    rgb = np.array(df.iloc[:,1:4].values)
    vec = np.reshape(vec,(1,-1))
    vec = np.repeat(vec,len(rgb),axis = 0)
    dist = LA.norm(rgb-vec,axis=1)
    return df.Color.values[dist.argmin()]