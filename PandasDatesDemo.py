#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020-04-21
by Jibin Joseph -joseph57
Tutorial - Time Series Analysis with Pandas
Analysis of Several times series data (AO- Arctic Oscillation and NO-North Atlantic Oscillation)

Revision 01-2020-04-21
Modified to add comments
"""
## Module Import
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
## Panel is not required incompleting the tutorial
import matplotlib.pyplot as plt
import os
import datetime

#pd.set_option('display.max_rows',15) # this limit maximum number of rows

## Displays the verison of Pandas
print(pd.__version__)

## Access AO Data
## Next line may be commented as it would download file and does not overwrite the existing file
os.system('/bin/wget "http://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/monthly.ao.index.b50.current.ascii" monthly.ao.index.b50.current.ascii')
ao=np.loadtxt('monthly.ao.index.b50.current.ascii')
print(ao.shape)

## Create the range of dates for our time series
dates=pd.date_range('1950-01',periods=ao.shape[0],freq='M')
print(dates)

## Create our first time series and dfifferent plots
AO=Series(ao[:,2],index=dates)
print(AO)
## Plot and save the Daily Atlantic Oscillation (AO) plot
AO.plot()
plt.title("Daily Atlantic Oscillation")
plt.xlabel("Times (in YYYY-MM)")
plt.ylabel("Oscillation")
plt.savefig("PDD_1_DailyAtlanticOscillation_plot.png")
plt.close()
## Misc Figures
AO['1980':'1990'].plot()
plt.close()
AO['1980-06':'1981-03'].plot()
plt.close()
## Reference the time periods
print(AO[120])
print(AO['1960-01'])
print(AO['1960'])
## Condition statement
print(AO[AO>0])

## Access NOA Time Series
## Next line may be commented as it would download file and does not overwrite the existing file
os.system('/bin/wget "https://www.cpc.ncep.noaa.gov/products/precip/CWlink/pna/norm.nao.monthly.b5001.current.ascii" norm.nao.monthly.b5001.current.ascii')
nao=np.loadtxt('norm.nao.monthly.b5001.current.ascii')

## Display head and tail anf length to check the date consistency
print("Dates:ao")
print(ao[:2])
print(ao[-2:])
print("Dates:nao")
print(nao[:2])
print(nao[-2:])
print("Length")
print(len(ao))
print(len(nao))

## Create a series
dates_nao=pd.date_range('1950-01',periods=nao.shape[0],freq='M')
NAO=Series(nao[:,2],index=dates_nao)
print(NAO)
print(NAO.index)
aonao=DataFrame({'AO':AO,'NAO':NAO})
aonao.plot(subplots=True)
plt.close()
print(aonao.head())
print(aonao.tail())
print(aonao['NAO'])
print(aonao.NAO)
aonao['Diff']=aonao['AO']-aonao['NAO']
print(aonao.head())
del aonao['Diff']
print(aonao.tail())

## Crazy Combination
aonao.loc[(aonao.AO>0)&(aonao.NAO<0) &\
           (aonao.index>datetime.datetime(1980,10,1)) &\
           (aonao.index<datetime.datetime(1989,1,1)),\
           'NAO'].plot(kind='barh')
plt.close()
## Statitics
print(aonao.mean())
print(aonao.max())
print(aonao.min())

## Row wise mean
print(aonao.mean(1))

print(aonao.describe())

## Resampling
AO_mm=AO.resample("A").mean()
AO_mm.plot(style='g--')
plt.title("Annual Median Values\n(for AO)")
plt.xlabel("Times (in YYYY)")
plt.ylabel("Oscillation")
plt.savefig("PDD_2_AnnualMedianValues_plot.png")
plt.close()

AO_mmedian=AO.resample("A").median()
AO_mmedian.plot()
plt.close()

AO_mmedian3A=AO.resample("3A").apply(np.max)
AO_mmedian3A.plot()
plt.close()

AO_mm=AO.resample("A").apply(['mean',np.min,np.max])
AO_mm['1900':'2000'].plot(subplots=True)
plt.close()
AO_mm['1900':'2000'].plot()
plt.close()
print(AO_mm.head())


## Moving Statistics
aonao.rolling(window=12,center=False).mean().plot(style='-g')
plt.title("Rolling Mean\n(for AO & NAO)")
plt.xlabel("Times (in YYYY-MM)")
plt.ylabel(" Mean Oscillation")
plt.savefig("PDD_3_RollingMean_plot.png")
plt.close()

## Rolling Correlation
aonao.AO.rolling(window=120).corr(other=aonao.NAO).plot(style='-g')
plt.close()

print(aonao.corr())