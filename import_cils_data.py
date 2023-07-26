import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

df = pd.read_stata("20520-0001-Data.dta",convert_categoricals=False)

ids = ['CASEID']
cols = df.columns.tolist()
cols.remove('CASEID')

parents = []
first = []
second = []
third = []
derived = []

def convert(s):
    while s:
        try:
            return int(s)
        except:
            s = s[:-1]

for col in cols:
    if col[0] == 'P':
        parents.append(col)
    elif col[0] == 'C':
        derived.append(col)
    else: #first char is V
        num = convert(col[1:])//100
        if num == 0 or num == 1:
            first.append(col)
        elif num == 2 or num == 3:
            second.append(col)
        else: #400
            third.append(col)

#df.drop(['V1']) #don't need an additional case id

d1 = df[list(itertools.chain.from_iterable([first, derived]))] #todo: need to edit bc techncially can't have all dervied data
#todo: add in the target variables from 2nd survey individually

d2 = df[list(itertools.chain.from_iterable([first, second, derived]))]
d2['V422'] = df['V422']
d2.dropna(subset = ['V422'], inplace=True)

def pearson(data, target, threshold):
    '''
    data: dataframe
    target: (string) target variable
    threshold: correlation threshold
    '''
    target_col = data[target]
    corr = abs(data.corr(method='pearson')[target].sort_values(ascending=False)[1:]) #got rid of , numeric_only=False
    features = corr[corr>=threshold]
    data = data[features.index]
    data[target] = target_col
    print(data) #todo:delete
    for col in data.columns:
        print(col)
    return data

d1 = pearson(d2, 'V422', 0.1)

#principal component analysis

#create ur new variables/run PCA

   
#df.to_csv(target + "_" + limiter + ".csv", sep=',', index=False, encoding='utf-8') #save to csv