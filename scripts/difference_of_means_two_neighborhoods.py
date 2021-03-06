
import pandas as pd
import numpy as np
import math

path = r'C:\Users\angelddaz\OneDrive\Documents\Data Training\data\RawDelData.csv'
data = pd.read_csv(path)

df = pd.DataFrame(data, columns = ['Tip', 'PersonWhoDelivered'])

#MUCH BETTER WAY
gcDels = data.loc[data['Area(text)']=='Garden City'][['Tip']]
hsDels = data.loc[data['Area(text)']=='Hidden Springs'][['Tip']]
bDels = gcDels+hsDels

#OLD INEFFICIENT METHOD OF "QUERYING" THE DATA
#angel = df['PersonWhoDelivered'] == 'Angel'
#sam = df['PersonWhoDelivered'] == 'Sammie'
#aDels = df[angel]
#sDels = df[sam]
#aDeliveries = aDels[['Tip']]
#sDeliveries = sDels[['Tip']]
#aDels = aDeliveries
#sDels = sDeliveries

mu_gc = gcDels.mean() #GC Delivery mean = 2.96
mu_hs = hsDels.mean() #HS Delivery mean = 5.24

sigma_gc = gcDels.std() #GC stdev = 2.0829
sigma_hs = hsDels.std() #HS stdev = 1.9950

variance_gc = gcDels.std() * gcDels.std() #GC variance = 4.3386
variance_hs = hsDels.std() * hsDels.std() #HS variance = 3.9799

n_gc = gcDels.count() #GC sample size = 221
n_hs = hsDels.count() #HS sample size = 34

degfreedom = n_gc + n_hs - 2 -1 #n-k-1: degrees of freedom = 252

#This is where the Hypothesis starts:
#Two Sample T Test
den1 = variance_gc/n_gc 
den2 = variance_hs/n_hs 
den3 = den1+den2      
den = math.sqrt(den3) 
num = mu_gc - mu_hs    

t = num/den #t stat: -6.166

#H0 : mu_a = mu_s
#Ha: mu_a != mu_s
#Degrees of freedom: df = 
#significance level: 0.05
#therefore, critical value = 1.9673

#We fail to reject the null hypothesis, and the result is not
#statistically significant at p < .05
#P-Value is 0.3775

####################################################################
#Ok, but what about random samples?
aRand = aDels.sample(n=400)
sRand = sDels.sample(n=400)
aDels = aRand
sDels = sRand
#still not statistically significant!