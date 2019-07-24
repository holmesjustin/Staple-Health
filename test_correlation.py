#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:08:05 2019

@author: JustinHolmes
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import random

df = pd.read_csv("/Users/JustinHolmes/Desktop/Staple Health/County/Mental Health Data/Concatenated_Data/US_County_All_Data_62719.csv", skiprows = 0, sep = ',', header = 0, dtype = {'FIPS': 'Int32'})
d = df[['Gini Index Estimate', '% Female', '% Non-Hispanic White', '% 65 and over', 'Household Income (In tens of thousands)', 'Mentally Unhealthy Days']]
# Compute the correlation matrix
corr = d.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})