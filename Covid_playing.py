#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 00:07:09 2020

@author: arsalanadil
"""

import numpy as np
import matplotlib.pyplot as plt


import csv

with open('/Users/arsalanadil/Desktop/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

data2 = np.array(data)

tempdata = np.delete(data2, [0,2,3], axis = 1)#remove unnecessary columns
#tempdata = np.hstack((tempdata, np.zeros((tempdata.shape[0], 1))))
size= np.shape(tempdata)

a = np.zeros((size[0]-1,size[1]-1)).astype(int)#integer array with #cases everyday
for i in range(1,size[0]):
    for j in range(1,size[1]):
        a[i-1][j-1] = int(tempdata[i][j])

Dict = {}
newsize = 0
i = 1
j = 0
while(i<(np.shape(tempdata)[0]-1)):
    if(tempdata[i][0] == tempdata[i+1][0]):
        a[j] = a[j] + a[j+1]
        a = np.delete(a,j+1,axis=0)
    else:
        j +=1
        Dict[tempdata[i][0]] = newsize
        newsize +=1
    i+=1
    
def getIndex(country):
    return Dict[country]

def getTimeStampFor(country):
    index = getIndex(country)
    return a[index]
    
def getTotalCasesEver():
    return np.sum(a[:,np.shape(a)[1]-1])

def casesSinceOnset(country):
    timeStamp = getTimeStampFor(country)
    i = 0
    while(timeStamp[i] == 0):
        i+=1
    
    return timeStamp[i:]

pkpop = 207.774 * 10**6
chinapop = 1.386 * 10**9
italypop = 60.48 * 10**6
uspop = 327.2 * 10**6
japanpop = 126.8 * 10**6
iranpop = 81.16 * 10**6
skpop = 51.47 * 10**6
indiapop = 1.339 * 10**9

pkpop_65 = 0.042 * pkpop
italypop_65 = .2169 * italypop
uspop_65 = 49.2 * 10**6
#skpop = 0

pk = casesSinceOnset('Pakistan')
china = casesSinceOnset('China')
italy = casesSinceOnset('Italy')
us = casesSinceOnset('US')
sk = casesSinceOnset('Korea, South')
uk = casesSinceOnset('United Kingdom')
iran = casesSinceOnset('Iran')
india = casesSinceOnset('India')
japan = casesSinceOnset('Japan')

#plt.plot(np.arange(pk.shape[0]),pk/pkpop * 10**6,
#         np.arange(30), italy[0:30]/italypop * 10**6 )

plt.plot(np.arange(pk.shape[0]),pk/pkpop * 10**6,
         np.arange(japan.shape[0]), japan/japanpop * 10**6 )

plt.plot(np.arange(sk.shape[0]), sk/skpop * 10**6,
         np.arange(pk.shape[0]),pk/pkpop * 10**6)


plt.plot(np.arange(iran.shape[0]),iran/iranpop * 10**6 )


plt.plot(np.arange(italy.shape[0]), italy/italypop * 10**6)

plt.plot(np.arange(us.shape[0]-30),us[30:]/uspop*10**5,
         np.arange(china.shape[0]),china/chinapop*10**5,
         )
        
    

