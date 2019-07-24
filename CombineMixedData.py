#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:24:57 2019

@author: JustinHolmes
"""

import pandas as pd

def combine(outfile = "/Users/JustinHolmes/Desktop/WeatherDataEdited.csv"):
   
    #Create the dataframe we are going to use
    dfBig = pd.read_csv("/Users/JustinHolmes/Desktop/allData.csv", sep = ',', skiprows = 1, header = 0)
    dfNew = pd.read_csv("/Users/JustinHolmes/Desktop/weatherData.csv", sep = ',', header = 0)
    print(dfBig.head())
    print("\n")
    print(dfNew.head())
    print("\n")
    
    for row in dfNew.itertuples():
        idx = 0
        print(row)
        #print(idx)
        print(row[1] + '; ' + row[2])
        #print(row[2])
        #print(dfBig['Name'][idx])
        #print(dfBig['Favorite Sport'][idx])
        while row[1] != dfBig['State'][idx] or row[2] != dfBig['County'][idx]:
            idx += 1
        print("Did Not Add this many times: ", idx)    
        print("Should Add to row: ", idx)
        dfBig['Days with AQI'][idx] = row[4]
        dfBig['Good Days'][idx] = row[5]
        dfBig['% Good Days'][idx] = row[6]
        dfBig['Moderate Days'][idx] = row[7]
        dfBig['Unhealthy for Sensitive Groups Days'][idx] = row[8]
        dfBig['Unhealthy Days'][idx] = row[9]
        dfBig['Very Unhealthy Days'][idx] = row[10]
        dfBig['Hazardous Days'][idx] = row[11]
        dfBig['Max AQI'][idx] = row[12]
        dfBig['90th Percentile AQI'][idx] = row[13]
        dfBig['Median AQI'][idx] = row[14]
        dfBig['Days CO'][idx] = row[15]
        dfBig['Days NO2'][idx] = row[16]
        dfBig['Days Ozone'][idx] = row[17]
        dfBig['Days SO2'][idx] = row[18]
        dfBig['Days PM2.5'][idx] = row[19]
        dfBig['Days PM10'][idx] = row[20]
        print(dfBig['% Good Days'][idx])
        #print("Added" + '\n')
        
    dfBig.to_csv(outfile, index = None)