#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:07:07 2019

@author: Johnny Chapman
CPSC 392
Linstead
Assignment 1

References:
https://stackoverflow.com/questions/41041364/how-to-stop-months-being-ordered-alphabetically-in-pandas-pivot-table
    
"""

import pandas as pd
import matplotlib.pyplot as plt


# Import data and set x and y variables
data = pd.read_csv(r'/Users/johnnychapman/Desktop/Chapman/FALL19/CPSC392/Datasets/forestfires.csv')
x = data.iloc[:,2]
y = data.iloc[:,8]

# Initialize month order
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
          'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# Reset month to date order not alphabetical
data['month'] = data['month'].astype('category', 
                                  ordered=True,
                               categories=months)
"""  
data['temp'] = data['temp'].astype('category', 
                                  ordered=True,
                                  categories=months)
"""
# Initialize variables
avg = data.groupby('month')['temp'].mean()
count = data.groupby('month')['month'].count()
#temp = data.groupby('month')['temp']
length = len(avg)
avgs = []
temps = []

# Add averages to a list
for i in range(0, length):
    avgs.append(avg[i])
    #temps.append(temp[i])
"""
# Plot graph
plt.bar(months, avgs)
plt.title('Average Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Average Temperature (Celcius)')
plt.show()




plt.hist(months, y)
plt.title('Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Temperature (Celcius)')
plt.show()


data2 = pd.read_csv(r'/Users/johnnychapman/Desktop/Chapman/FALL19/CPSC392/Datasets/winequality-red.csv')
alc = data2.iloc[:,10]
qual = data2.iloc[:,11]

alc_avg = data2.groupby('quality')['alcohol'].mean()
quals = ['3', '4', '5', '6', '7', '8']

print(alc_avg)
alc_avgs = []
length2 = len(alc_avg)
for n in range(0, length2):
    print(alc_avg[n])


plt.bar(qual, alc_avgs)
plt.title('Average Alochol by Quality')
plt.xlabel('Quality')
plt.ylabel('Average Alcohol Percentage')
plt.show()
"""

#print(alc_avgs)
#print(temp)