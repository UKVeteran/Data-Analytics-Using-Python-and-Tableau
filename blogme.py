# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:58:14 2023

@author: jau19
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

data=pd.read_excel(r'C:\Users\jau19\OneDrive\Desktop\Tableau\1 - Python and Tableau\Python\Project 3\articles.xlsx')

data.head(2)

data.info()

data.groupby(['source_id'])['article_id'].count()

data.groupby(['source_id'])['engagement_reaction_count'].sum()

data=data.drop('engagement_reaction_count',axis=1)



def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag

# Define the keyword
keywordflag= keywordflag('murder')


data['keyword_flag']=pd.Series(keywordflag)



# Create a SentimentIntensityAnalyzer instance
sentint = SentimentIntensityAnalyzer()

# Assuming you have a DataFrame 'data' with a 'title' column
text = data['title'][16]

# Analyze the sentiment of the text
sentiment = sentint.polarity_scores(text)


neg=sentiment['neg']
pos=sentiment['pos']
neu=sentiment['neu']


title_neg=[]
title_pos=[]
title_neu=[]

length = len(data)

for x in range(0,length):
    try:
        text=data['title'][x]
        sentint = SentimentIntensityAnalyzer()
        sentiment = sentint.polarity_scores(text)
        neg=sentiment['neg']
        pos=sentiment['pos']
        neu=sentiment['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg.append(neg)
    title_pos.append(pos)
    title_neu.append(neu)

title_neg=pd.Series(title_neg)

title_pos=pd.Series(title_pos)

title_neu=pd.Series(title_neu)


data['title_neg']=title_neg
data['title_pos']=title_pos
data['title_neu']=title_neu


data.to_excel(r'C:\Users\jau19\OneDrive\Desktop\Tableau\1 - Python and Tableau\Python\Project 3\blogme_clean.xlsx', index=False)