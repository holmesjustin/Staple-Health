#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:18:18 2019

@author: JustinHolmes
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import random
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def correlation():
    
    #Create the dataframe we are going to use
    df = pd.read_csv("/Users/JustinHolmes/Desktop/Staple Health/County/Mental Health Data/Concatenated_Data/US_County_All_Data_62719.csv", skiprows = 0, sep = ',', header = 0, dtype = {'FIPS': 'Int32'})
    
    #Change any values to get better-looking results
    #df['Household Income'] = df['Household Income'].apply(lambda x: x*.001)
    
    #Print the head of the dataframe to see if it imports correctly
    #print(df.head())
    
    #print(df.head())
    
    #Set the independent variables using the column names
    #ind1 = '% with SNAP'
    #ind2 = 'Average Daily PM2.5 (Air Pollution)'
    #ind3 = 'Association Rate'
    ind4 = 'Gini Index Estimate'
    #ind5 = '% Adult Obese'
    #ind6 = 'Teen Birth Rate'
    #ind7 = 'Life Expectancy

    #Set the control variables using the column names
    ctl1 = '% Female'
    ctl2 = '% Non-Hispanic White'
    ctl3 = '% 65 and over'
    ctl4 = 'Household Income (In tens of thousands)'
    ctl5 = 'AVERAGE LEVEL OF EDUCATION'
    
    #Set the dependent variable using the column name
    dep1 = 'Mentally Unhealthy Days'
    #dep2 = 'Household Income (In tens of thousands)'
    
    
    #Following variables used for the regression analysis
    #X = df[[ind1, ind2, ind3, ind4, ind5]].iloc[0:100]
    X = df[[ind4, ctl1, ctl2, ctl3, ctl4]]
    Y = df[dep1]
    #sm.add_constant(X)
    
    #Y = Y.apply(lambda x: x + np.random.rand() * 1)
    #X = X + 1
    
    model = sm.OLS(Y, X, missing = 'drop')
    results = model.fit()
    print_model = results.summary()  
    #print(print_model)
    
    
    #Print plot to visualize relationship
    #plot = sns.jointplot(x=df[ind1], y=Y, data=df, kind = 'reg', joint_kws={'line_kws':{'color':'red'}})
    #print(plot)
    
    
    #Randomly select a county to use data for prediction
    #county = random.randint(1,len(df))
    
    #countyInd = df[ind4][county-2]
    
    #countyCTL1 = df[ctl1][county-2]
    #countyCTL2 = df[ctl2][county-2]
    #countyCTL3 = df[ctl3][county-2]
    #countyCTL4 = df[ctl4][county-2]
    
    #countyDEP = df[dep1][county-2]
    
    #prediction = results.predict([countyInd, countyCTL1, countyCTL2, countyCTL3, countyCTL4])[0]
    #error = (prediction-countyDEP)/countyDEP*100
    
    #print("Prediction: ", prediction)
    #print("Actual: ", countyDEP)
    #print("% Error: ", error)
    
    #return error
 
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=None)
    
    regressor = LinearRegression()  
    regressor.fit(X_train, y_train)
    
    coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])  
    #print(coeff_df)
    
    y_pred = regressor.predict(X_test)
    
    df1 = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(df1.head(25))
    
    
    graph = plt.bar(y_pred, y_test)
    print(graph)
    
    
    
    
    
"""
def avgError():
    
    i = 10
    errRec = []
    for n in range(i):
        err = correlation()
        errRec.append(abs(err))
        
    avgErr = sum(errRec)/len(errRec)
    print("Average error after", i, "trials:", avgErr,"%")
    
"""
    
    
    
    