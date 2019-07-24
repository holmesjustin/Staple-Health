#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:57:16 2019

@author: JustinHolmes
"""

import pandas as pd

def merge():
    
    dfNew = pd.read_csv("/Users/JustinHolmes/Desktop/Staple Health/County/Mental Health Data/Concatenated_Data/Concatenated_New.csv", sep = ',', skiprows = 0, header = 0)
    dfAll = pd.read_csv("/Users/JustinHolmes/Desktop/Staple Health/County/Mental Health Data/Concatenated_Data/US_County_All_Data_62019_Copy.csv", sep = ',', skiprows = 0, header = 0, dtype = {'FIPS': 'Int64'})
    print(dfNew.head())
    print(dfAll.head())
    dfEdited = dfAll.merge(dfNew, on = 'FIPS', how = 'left') 
    print(dfEdited.head())
    #print(dfEdited.head())
    #dfEdited["FIPS"] = dfEdited["FIPS"].astype(int)
    #print(dfEdited.head())
    dfEdited.to_csv("/Users/JustinHolmes/Desktop/US_County_All_Data_62719.csv", index = None)
