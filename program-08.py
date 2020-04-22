#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020-04-21
by Jibin Joseph -joseph57

Assignment 08 - Time Series Analysis with Python
Revision 031 - 2020-04-21
Modified to add comments
"""

## Import the required packages
import pandas as pd
import matplotlib.pyplot as plt

## Skip initial 25 lines
## Use Columns 3 and 4 for a single Datetime element (In Python - 2 & 3 columns)
## Use Column 5 (discharge in cubic feet per second) for the value (In Python - 4 column)
dd_data=pd.read_table("WabashRiver_DailyDischarge_20150317-20160324.txt",
                   delimiter='\t',header=23,skiprows=2,usecols=[2,3,4],
                   names=['Datetime','Timezone','Discharge'],
                   parse_dates=[['Datetime','Timezone']],index_col='Datetime_Timezone')
## Parse_dates converts the time from EST to UTC, may be useful when EDT and EST are found
## Use newly created Datetime_Timezone column as index
#print(dd_data.head())

## Create a plot of daily average streamflow for the period of record, 
## written to a PDF or PS file

daily_av_sf=dd_data.resample("D").mean() ## resample to daily from 15 min
#print(daily_av_sf.head())

ax=daily_av_sf.plot(y='Discharge',style='b--',label='Daily_Average')
plt.title("Plot of Daily Average Streamflow")
plt.xlabel("Time (days)")
plt.ylabel("Discharge (in cfs)")
plt.legend()
plt.tight_layout()
plt.savefig("SF_1_DailyAverageStreamflow_plot.ps")
plt.close()

## Using the daily average flow data, identify and plot the 10 days with highest flow, 
## written to a PDF or PS file. 
## Use symbols to represent the data on the same time axis used for the full 
## daily flow record.

highflow_10days=daily_av_sf.nlargest(10,'Discharge') ## find high 10 flows
#print(highflow_10days.head())

ax=daily_av_sf.plot(y='Discharge',style='b--',label='Daily_Average')
plt.scatter(highflow_10days.index,highflow_10days.Discharge,c='r', 
            marker='*',label='High10Flows')
plt.title("Plot of Daily Average Streamflow\n(with 10 days highest flow)")
plt.xlabel("Time (days)")
plt.ylabel("Discharge (in cfs)")
plt.legend()
plt.tight_layout()
plt.savefig("SF_2_DailyAverageStreamflow_WithHigh10Flows_plot.ps")
plt.close()

## Create a plot of monthly average streamflow for the period of record, 
## written to a PDF or PS file

month_av_sf=dd_data.resample("M").mean() ## resample to monthly from 15 min
#print(month_av_sf.head())

ax=month_av_sf.plot(y='Discharge',style='b--',label='Monthly_Average')
plt.title("Plot of Monthly Average Streamflow")
plt.xlabel("Time (months)")
plt.ylabel("Discharge (in cfs)")
plt.legend()
plt.tight_layout()
plt.savefig("SF_3_MonthlyAverageStreamflow_plot.ps")
plt.close()