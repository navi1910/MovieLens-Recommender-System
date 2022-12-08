# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 18:02:28 2022

@author: Navi
"""
# Movie Recommender System using MoviesLen Data.
##To recommendend Movies according to the ratings provided by other users. 
##This is an example of Collaborative Filtering method in Recommender Systems.

# Imports
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the data
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
data = pd.read_table('u.data', names = column_names)
data.head()

# Checking the basic info about the data.
data.isnull().sum()

data.info()

# Loading the other table
movie_titles = pd.read_csv('Movie_Id_Titles')
movie_titles.head()

# Merging both the tables
df = pd.merge(data, movie_titles, on = 'item_id')
df.head()

# Creating dataframe for Average ratings and count of ratings for each title.
rating = pd.DataFrame()
rating['avg_rating'] = df.groupby('title')['rating'].mean()
rating['Count of ratings'] =  df.groupby('title')['rating'].count()
rating.head()


# Simple Exploratory Data Analysis and Data Visualizations.
sns.set_style('white')
sns.jointplot(data = rating, x = 'avg_rating', y = 'Count of ratings', 
              color = 'green', alpha = 0.5)

rating['avg_rating'].hist(bins = 80)
plt.title('Average Rating')

rating['Count of ratings'].hist(bins = 80)
plt.title('Count of Ratings')

# Creating a pivot table for Ratings.
matrix = pd.pivot_table(data = df, columns = 'title', index = 'user_id', 
                        values = 'rating')
matrix.head()

# Creating the Recommender Process.
dalmatians = matrix['101 Dalmatians (1996)']
dalmatians

similar_to_dalmatians = matrix.corrwith(dalmatians).sort_values(ascending 
                                                                = False)

similar_to_dalmatians = pd.DataFrame(similar_to_dalmatians, 
                                     columns=['Correlation'])
similar_to_dalmatians = similar_to_dalmatians.join(rating['Count of ratings'])
similar_to_dalmatians.head()

similar_to_dalmatians[similar_to_dalmatians['Count of ratings'] > 100].head()

# Defining the Function
def recommender(text):
    ratings = matrix[text]
    similar = matrix.corrwith(ratings).sort_values(ascending = False)
    similar = pd.DataFrame(similar,columns=['Correlation'])
    similar = similar.join(rating['Count of ratings'])
    return similar[(similar['Count of ratings']> 100) & 
                   similar['Correlation']>0.4].sort_values('Correlation',
                                                           ascending = False).head(10)

recommender('Star Wars (1977)')

recommender('Pinocchio (1940)')

recommender('Dumbo (1941)')