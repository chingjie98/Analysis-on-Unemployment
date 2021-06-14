#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 15:00:02 2021

@author: joanntan
"""
### A3 POSTER PAGE 2 (ABSENTEEISM FROOM WORK)
# Note: If output prompts 'No such file in directory', kindly replace the file pathname in pd.read_csv.

##BAR GRAPH: TOP 5 REASONS FOR ABSENTEEISM 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

absentees = pd.read_csv("/Users/joanntan/Desktop/PYTHON PROJECT/PART 2/absentees_cleaned_data.csv")
rfa = absentees['Reason for absence'].value_counts().head()
colours = ['steelblue','skyblue', 'lightskyblue','silver','lightslategrey']
MC = mpatches.Patch(color='steelblue', label='#1: Medical Consultation')
DC = mpatches.Patch(color='skyblue', label='#2: Dental Consultation')
Physio = mpatches.Patch(color='lightskyblue', label='#3: Physiotherapy')
Disease = mpatches.Patch(color='silver', label='#4: Diseases of the musculoskeletal system and connective tissue')
Others = mpatches.Patch(color='lightslategrey', label='#5: Injury, poisoning and certain other consequences of external causes')
ay1 = rfa.plot(kind='barh', color = colours)
ay1.set_title("Top 5 Reasons for Absenteeism", fontweight='bold',fontsize='16')
ay1.set_ylabel("(Reason for Absence)",size='13')
ay1.set_xlabel("(Frequency)", size='13')
plt.legend(handles=[MC,DC,Physio,Disease,Others],loc=(1.05,0))


## CORRELATION BETWEEN BMI AND ABSENTEEISM
df = pd.read_csv("/Users/joanntan/Desktop/PYTHON PROJECT/PART 2/absentees_cleaned_data.csv")
y = df.iloc[:,-2:]
print (y)
y.corr(method ='pearson') # -0.037202, NEGATIVE CORRELATION


## SCATTER GRAPH: RELATIONSHIP BETWEEN BMI AND ABSENTEEISM
df = pd.read_csv("/Users/joanntan/Desktop/PROJECT/Cleaned_data/absentees_cleaned.csv")
x = df["BMI"]
y = df["Absenteeism"]
print(np.corrcoef(x, y))
plt.scatter(x, y, color = '#4682b4', s = 12) 
plt.title('Relationship between BMI and Absenteeism Rate')
plt.xlabel('BMI')
plt.ylabel('Absenteeism (in hours)')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='#E34856')
plt.show()


## AVERAGE ABSENTEEISM RATE FOR PEOPLE WITH HEALTHY (18 - 24) AND UNHEALTHY BMI (ABOVE 24)
x = df[(df.BMI >= 18) & (df.BMI <= 24)].Absenteeism.mean()
print (x) #7.1333 hours
y = df[(df.BMI > 24)].Absenteeism.mean()
print (y) #7.8747 hours


## MINIMUM AND MAXIMUM BMI
x = df["BMI"].min()
print (x) #19
y = df["BMI"].mean()
print (y) #26.5263

##PIE CHART: PROPORTION OF HEALTHY AND UNHEATLHY BMI EMPLOYEES
y = df[(df.BMI > 24)].Absenteeism.count()
print (y) #423 employees
a = df[(df.BMI < 24)].Absenteeism.count()
print (a) #161 employees

Proportion = [423,161]
my_labels = 'Healthy BMI', 'Overweight, Obese and Extremely Obese'
my_colors = ['lightblue','lightsteelblue']
my_explode = (0, 0.1)
plt.pie(Proportion, labels=my_labels, autopct='%1.1f%%', startangle=15, shadow = True, colors=my_colors, explode=my_explode)
plt.title('Proportion of Employees (BMI)')
plt.axis('equal')
plt.show()

## SCATTER GRAPH: EMPLOYEES WITH HEALTHY BMI AND ABSENTEEISM
x = df['BMI'][(df.BMI >= 18) & (df.BMI <= 24)]
print (x)
y = df[(df.BMI >= 18) & (df.BMI <= 24)].Absenteeism
print (y)
a = x
b = y 
print(np.corrcoef(a, b)) # -0.01504443, NEGATIVE CORRELATION
plt.scatter(x, y, color = '#00bfff', s = 10)
plt.title('Do healthier employees have a lower absenteeism rate?')
plt.xlabel('Healthy BMI Range')
plt.ylabel('Absenteeism (in hours)')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='#E34856')
plt.show()


## AVERAGE AND MAXIMUM ABSENTEEISM RATE FOR EMPLOYEES WITH HEALTHY BMI 
x = df['BMI'][(df.BMI >= 18) & (df.BMI <= 24)]
print (x)
y = df[(df.BMI >= 18) & (df.BMI <= 24)].Absenteeism
print (y)
maxab = y.max()
print (maxab) #120 hours
meanab = y.mean()
print (meanab) #7.1333 hours


##CORRELATION BETWEEN WORKLAOD AND ABSENTEEISM RATE 
x = df["Workload"] #Workload = average work load per day 
y = df["Absenteeism"]
z = x.corr(y)
print (z) #0.024351532740927367, POSITIVE CORRELATION


##ABSENTEEISM RATE FOR EMPLOYEES WITH THE LOWEST WORKLOAD
lowest_workload = df["Workload"].min()
print (lowest_workload) #205.917

df[df.Workload == 205.917].ID
df[df.Workload == 205.917].Absenteeism

x = ["1","2","3","10","11","18","19","20","30","33"]
y = [4,24,13,48,25,8,4,8,4,2]

plt.bar(x, y, color = '#9acd32', align='center',width=0.5)
plt.title('Total Absenteeism Rate among Employees with the Lowest Workload')
plt.xlabel('Employees ID Number')
plt.ylabel('Total Absenteeism Rate (in hours)')
plt.xticks(x, rotation='horizontal')
plt.show()


##ABSENTEEISM RATE FOR EMPLOYEES WITH THE HIGHEST WORKLOAD
highest_workload = df["Workload"].max()
print (highest_workload) #378.884

df[df.Workload == 378.884].ID
df[df.Workload == 378.884].Absenteeism

x = ["3","10","11","14","27","28","36"]
y = [93,27,60,75,21,24,31]

plt.bar(x, y, color = '#006400', align='center',width=0.5)
plt.title('Total Absenteeism Rate among Employees with the Highest Workload')
plt.xlabel('Employees ID Number')
plt.ylabel('Total Absenteeism Rate (in hours)')
plt.xticks(x, rotation='horizontal')
plt.show()





