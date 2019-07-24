#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:19:34 2019

@author: JustinHolmes
"""

3144
import pandas as pd

def fixRatio():
    
    df = pd.read_csv("/Users/JustinHolmes/Desktop/Staple Health/County/Mental Health Data/Concatenated_Data/US_County_All_Data_62719.csv", sep = ',', header = 0)
    
    c = 0
    idx = 0
    for row in df.itertuples():
        #print(type(row[66]))
        #print(row[66])
        if c < 3144:
            
            if type(row[66]) == str:
                fix1 = row[66].split(":")[0]
                df['Other PCP Ratio'][idx] = fix1
            
            if type(row[203]) == str:  
                fix2 = row[203].split(":")[0]
                df['PCP Ratio'][idx] = fix2
            
            if type(row[207]) == str:
                fix3 = row[207].split(":")[0]
                df['Dentist Ratio'][idx] = fix3
            
            if type(row[211]) == str:
                fix4 = row[211].split(":")[0]
                df['MHP Ratio'][idx] = fix4
             
            c += 1
            idx +=1
            
       
        else:
            break
        
    #print(df['Other PCP Ratio'][0:5])
    
    
    df.to_csv("/Users/JustinHolmes/Desktop/Test.csv", index = None)