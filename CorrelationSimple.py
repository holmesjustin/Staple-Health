#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:12:32 2019

@author: JustinHolmes
"""

import pandas as pd

def correlation():
    
    df = pd.read_csv("/Users/JustinHolmes/Desktop/Staple Health/Mental Health County Data/Concatenated_Data/US_County_Data_Sorted_Snaps.csv", skiprows = 3, sep = ',', header = None)
    print(df.head)
    
    val = df[3].corr(df[35])
    print(val)