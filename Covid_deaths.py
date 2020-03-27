#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 02:38:30 2020

@author: arsalanadil
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

import Covid_playing as cases

with open('/Users/arsalanadil/Desktop/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', newline='') as csvfile:
    death_data = list(csv.reader(csvfile))

death_data2 = np.array(death_data)

deathtempdata = np.delete(death_data2, [0,2,3], axis = 1)#remove unnecessary columns
#tempdata = np.hstack((tempdata, np.zeros((tempdata.shape[0], 1))))
size= np.shape(deathtempdata)

death_arr = np.zeros((size[0]-1,size[1]-1)).astype(int)#integer array with #cases everyday
for i in range(1,size[0]):
    for j in range(1,size[1]):
        death_arr[i-1][j-1] = int(deathtempdata[i][j])

Dict = {}
newsize = 0
i = 1
j = 0
while(i<(np.shape(deathtempdata)[0]-1)):
    if(deathtempdata[i][0] == deathtempdata[i+1][0]):
        death_arr[j] = death_arr[j] + death_arr[j+1]
        death_arr = np.delete(death_arr,j+1,axis=0)
    else:
        j +=1
        Dict[deathtempdata[i][0]] = newsize
        newsize +=1
    i+=1
    
def getDeathIndex(country):
    return Dict[country]

def getDeathTimeStampFor(country):
    index = getDeathIndex(country)
    return death_arr[index]
    
def getTotalDeathsEver():
    return np.sum(death_arr[:,np.shape(death_arr)[1]-1])

def deathsSinceOnset(country):
    casestimeStamp = cases.getTimeStampFor(country)#since first case
    timeStamp = getDeathTimeStampFor(country)#array containing deaths
    i = 0
    while(casestimeStamp[i] == 0):
        i+=1
    
    return timeStamp[i:]


pk_d = deathsSinceOnset('Pakistan')
china_d = deathsSinceOnset('China')
italy_d = deathsSinceOnset('Italy')
us_d = deathsSinceOnset('US')
sk_d = deathsSinceOnset('Korea, South')
iran_d = deathsSinceOnset('Iran')


#plt.plot( 
#        np.arange(26), italy[0:26]//(cases.casesSinceOnset('Italy')[0:26]) * 10**6,
#                 np.arange(pk.shape[0]), pk/cases.casesSinceOnset('Pakistan') * 10**6)

plt.plot( 
        np.arange(italy_d.shape[0]), 
        np.divide(italy_d,(cases.casesSinceOnset('Italy')))*100)

plt.plot( 
        np.arange(us_d.shape[0]-20), 
        np.divide(us_d,(cases.casesSinceOnset('US')))[20:]*100)


plt.plot( 
        np.arange(pk_d.shape[0]), 
        np.divide(pk_d,(cases.casesSinceOnset('Pakistan')))*100)


plt.plot( 
        np.arange(sk_d.shape[0]), 
        np.divide(sk_d,(cases.casesSinceOnset('Korea, South')) )*100)


plt.plot( 
        np.arange(italy_d.shape[0]), 
        np.divide(italy_d,cases.italypop_65 )*100)

plt.plot( 
        np.arange(us_d.shape[0]-30), 
        np.divide(us_d,cases.uspop_65 )[30:]*100)

plt.plot( 
        np.arange(pk_d.shape[0]), 
        np.divide(pk_d,cases.pkpop_65 )*100)



#plt.plot(np.arange(us.shape[0]-30),us[30:]/uspop*10**5,
#         np.arange(china.shape[0]),china/chinapop*10**5,
#         )
        
    

