# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 05:34:43 2023

@author: jau19
"""

import pandas as pd

data = pd.read_csv(r'C:\Users\jau19\OneDrive\Desktop\Tableau\1 - Python and Tableau\Python\Project 1\transaction2.csv',sep=';')

data.shape

data.info()



CostPerItem=11.73
SellingPricePerItem=21.11
NumberofItemsPurchased=6

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction=NumberofItemsPurchased*CostPerItem
SellingPricePerTransaction=NumberofItemsPurchased*SellingPricePerItem

CostPerItem=data['CostPerItem']
NumberofItemsPurchased=data['NumberOfItemsPurchased']
CostPerTransaction=CostPerItem*NumberofItemsPurchased

data['CostPerTransaction']=data['CostPerItem']*data['NumberOfItemsPurchased']
data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']
data['ProfitPerTransaction']=data['SalesPerTransaction']-data['CostPerTransaction']

data['Markup']=(data['SalesPerTransaction']-data['CostPerTransaction'])/data['CostPerTransaction']


roundmarkup=round(data['Markup'],2)
data['Markup'] = round(data['Markup'],2)



my_name = 'Johar' + 'M'
my_date = 'Day' + '-' + 'Month' + '-' + 'Year'

# Assuming you have a DataFrame named 'data'
my_date_column = data['Day'].astype(str) + '-'

print(my_date_column.dtype)

day=data['Day'].astype(str)
year=data['Year'].astype(str)
print(day.dtype)
print(year.dtype)


my_date=day + '-' +data['Month'] + '-' + year
data['date']=my_date


data.iloc[0]
data.iloc[0:3]
data.iloc[-5]


data.head(5)


data.iloc[:,2]

data.iloc[4,2]


split_col=data['ClientKeywords'].str.split(',',expand=True)

data['ClientAge']=split_col[0]
data['ClientType']=split_col[1]
data['LengthofContract']=split_col[2]


data['ClientAge']=data['ClientAge'].str.replace('[','')
data['LengthofContract']=data['LengthofContract'].str.replace(']','')

data['ItemDescription']=data['ItemDescription'].str.lower()



seasons=pd.read_csv(r'C:\Users\jau19\OneDrive\Desktop\Tableau\1 - Python and Tableau\Python\Project 1\value_inc_seasons.csv',sep=';')


data= pd.merge(data, seasons, on='Month')


data=data.drop('ClientKeywords', axis=1)
data=data.drop('Day', axis=1)
data=data.drop(['Year', 'Month'], axis=1)

data.to_csv('C:\\Users\\jau19\\OneDrive\\Desktop\\Tableau\\1 - Python and Tableau\\Python\\Project 1\\ValueInc_Cleaned.csv', index=False)