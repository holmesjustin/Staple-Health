#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 08:41:57 2019

@author: JustinHolmes
"""

import os
import glob
import pandas as pd
#import csv


def concatenate(indir="/Users/JustinHolmes/Desktop/Staple Health/County/Mental Health Data/Raw_Data", outfile = "/Users/JustinHolmes/Desktop/Concatenated.csv"):
    os.chdir(indir)
    fileList = glob.glob("*.csv")
    dfList = []
    #colnames = headers
    for file in fileList:
        print(file)
        df = pd.read_csv(file, skiprows = 3, header = None)
        dfList.append(df)
    concatDf = pd.concat(dfList, axis = 0)
    #concatDf.columns = colnames
    concatDf.to_csv(outfile, index = None)
    