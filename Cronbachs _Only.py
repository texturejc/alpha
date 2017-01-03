# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 11:54:03 2016

@author: James Carney
"""

import scipy.stats as sp
import random
import csv
import pandas as pd
import numpy as np

filepath = input('Please enter the filepath: ') 


data = pd.read_csv(filepath, encoding = 'latin-1')




################# Cronbach's Alpha next

### Seeing

Seeing = [col for col in data.columns if 'seeing' in col]
Seeing_df = []

for i in Seeing:
    Seeing_df.append(data[i])

Seeing_df1 = pd.concat(Seeing_df, axis=1)

Seeing_df2 = Seeing_df1.dropna()


itemvars_seeing = Seeing_df2.var(axis=0, ddof = 1)
tscores_seeing = Seeing_df2.sum(axis=1)
nitems_seeing = len(Seeing_df2.columns)

C_alpha_seeing = nitems_seeing / (nitems_seeing-1.) * (1 - itemvars_seeing.sum() / tscores_seeing.var(ddof=1))

### Hearing

Hearing = [col for col in data.columns if 'hearing' in col]
Hearing_df = []

for i in Hearing:
    Hearing_df.append(data[i])

Hearing_df1 = pd.concat(Hearing_df, axis=1)

Hearing_df2 = Hearing_df1.dropna()


itemvars_hearing = Hearing_df2.var(axis=0, ddof = 1)
tscores_hearing = Hearing_df2.sum(axis=1)
nitems_hearing = len(Hearing_df2.columns)

C_alpha_hearing = nitems_hearing / (nitems_hearing-1.) * (1 - itemvars_hearing.sum() / tscores_hearing.var(ddof=1))

### Tasting

Tasting = [col for col in data.columns if 'tasting' in col]

Tasting_df = []

for i in Tasting:
    Tasting_df.append(data[i])

Tasting_df1 = pd.concat(Tasting_df, axis=1)

Tasting_df2 = Tasting_df1.dropna()


itemvars_tasting = Tasting_df2.var(axis=0, ddof = 1)
tscores_tasting = Tasting_df2.sum(axis=1)
nitems_tasting = len(Tasting_df2.columns)

C_alpha_tasting = nitems_tasting / (nitems_tasting-1.) * (1 - itemvars_tasting.sum() / tscores_tasting.var(ddof=1))

#### Touching

Touching = [col for col in data.columns if 'touch' in col]

Touching_df = []

for i in Touching:
    Touching_df.append(data[i])

Touching_df1 = pd.concat(Touching_df, axis=1)

Touching_df2 = Touching_df1.dropna()


itemvars_touching = Touching_df2.var(axis=0, ddof = 1)
tscores_touching = Touching_df2.sum(axis=1)
nitems_touching = len(Touching_df2.columns)

C_alpha_touching = nitems_touching / (nitems_touching-1.) * (1 - itemvars_touching.sum() / tscores_touching.var(ddof=1))

#### Smelling

Smelling = [col for col in data.columns if 'smelling' in col]

Smelling_df = []

for i in Smelling:
    Smelling_df.append(data[i])

Smelling_df1 = pd.concat(Smelling_df, axis=1)

Smelling_df2 = Smelling_df1.dropna()


itemvars_Smelling = Smelling_df2.var(axis=0, ddof = 1)
tscores_Smelling = Smelling_df2.sum(axis=1)
nitems_Smelling = len(Smelling_df2.columns)

C_alpha_smelling = nitems_Smelling / (nitems_Smelling-1.) * (1 - itemvars_Smelling.sum() / tscores_Smelling.var(ddof=1))

#### Body

Body = [col for col in data.columns if 'body' in col]

Body_df = []

for i in Body:
    Body_df.append(data[i])

Body_df1 = pd.concat(Body_df, axis=1)

Body_df2 = Body_df1.dropna()


itemvars_Body = Body_df2.var(axis=0, ddof = 1)
tscores_Body = Body_df2.sum(axis=1)
nitems_Body = len(Body_df2.columns)

C_alpha_body = nitems_Body / (nitems_Body-1.) * (1 - itemvars_Body.sum() / tscores_Body.var(ddof=1))

### Outputs


print ('\n'+'Cronbach\'s alpha for seeing is '+str(C_alpha_seeing))
print ('Cronbach\'s alpha for hearing is '+str(C_alpha_hearing))
print ('Cronbach\'s alpha for tasting is '+str(C_alpha_tasting))
print ('Cronbach\'s alpha for touching is '+str(C_alpha_touching))
print ('Cronbach\'s alpha for smelling is '+str(C_alpha_smelling))
print ('Cronbach\'s alpha for the body is '+str(C_alpha_body))




    
    

    
    


    