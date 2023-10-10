# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 06:38:21 2023

@author: jau19
"""


import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Use double backslashes or a raw string for the file path
json_file = open(r'C:\Users\jau19\OneDrive\Desktop\Tableau\1 - Python and Tableau\Python\Project 2\loan_data_json.json', 'r')
data = json.load(json_file)


with open(r'C:\Users\jau19\OneDrive\Desktop\Tableau\1 - Python and Tableau\Python\Project 2\loan_data_json.json') as json_file:
    data=json.load(json_file)
    print(data)


lists=['apple','banana','pear','pear']
lists.append('cherry')

lists.insert(1,'grape')

lists.remove('pear')

lists.pop()


mydict={
        'name':'Johar',
        'location':'UK',
        'favcolor':'black',
        'luckynumber':31
        }

color=mydict['favcolor']
print(color)



mydict.keys()
mydict.values()


mydict.items()


mydict['gender']='male'
print(mydict)



loandata=pd.DataFrame(data)

loandata['purpose'].unique()

loandata.describe()


loandata['int.rate'].describe()

loandata['fico'].describe()

loandata['dti'].describe()


income=np.exp(loandata['log.annual.inc'])
loandata['annualincome']=income


arr = np.array([1, 2, 3, 4])

arr = np.array(43)


a=40
b=500

if b>a:
    print('b>a')


a=40
b=500
c=1000

if b>a and b<c:
    print('b is greater than a but is less than c')



length=len(loandata)
ficocat=[]
for x in range(0,10):
    category =loandata['fico'][x]

    try:
        if category >=300 and category <400:
            cat='Very Poor'
        elif category >=400 and category <600:
            cat='Poor'
        elif category >=601 and category <660:
            cat='Fair'
        elif category >=660 and category <700:
            cat='Good'
        elif category >=700:
            cat='Excellent'
        else:
            cat='Unknown'
    except:
        cat='Unknown'
    ficocat.append(cat)
    
ficocat=pd.Series(ficocat)

loandata['fico.category']=ficocat



loandata.loc[loandata['int.rate']>0.12, 'int.rate.type']='High'
loandata.loc[loandata['int.rate']<=0.12, 'int.rate.type']='Low'


catplot=loandata.groupby(['fico.category']).size()
catplot.plot.bar(width=0.1)


catplot=loandata.groupby(['purpose']).size()
catplot.plot.bar(width=0.1)


ypoint=loandata['annualincome']
xpoint=loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()

loandata.to_csv('C:\\Users\\jau19\\OneDrive\\Desktop\\Tableau\\1 - Python and Tableau\\Python\\Project 2\\loan_cleaned.csv', index=True)