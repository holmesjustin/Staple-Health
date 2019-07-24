#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:12:43 2019

@author: JustinHolmes
"""

import pandas as pd

def fixFIPS():
    
    df = pd.read_csv("/Users/JustinHolmes/Desktop/WeatherData2014.csv", sep = ',', header = 0)
    print(df.head())
    c = 0
    idx = 0
    for row in df.itertuples():
        if c < 3108:
            #print(row[2])
            if row[2][1] == 0:
                fix = row[2][2]+row[2][4:7]
            else:
                fix = row[2][1:3]+row[2][4:7]
            #print(fix)
            df['FIPS'][idx] = fix
            #print(row)
            c += 1
            idx += 1
            
    #print(df.head())
    df.to_csv('temp.csv', index=False)
    df = pd.read_csv('temp.csv', sep = ',', header = 0, dtype={'FIPS': 'Int64'})
    print(df.head())
    df.to_csv("/Users/JustinHolmes/Desktop/WeatherDataFIPS2014.csv", index = None)