#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:41:26 2019

@author: JustinHolmes
"""

import pandas as pd

def cutRows():
    
    df = pd.read_csv("/Users/JustinHolmes/Desktop/US_county_2015_annualtmean.csv", sep = ',', header = 0)
    dfNew = df[df.TIME > 2013]
    print(dfNew.head())
    
    
    dfNew.to_csv("/Users/JustinHolmes/Desktop/WeatherData2014.csv", index = None)