# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 18:02:30 2022

@author: Navi
"""

# Final Function which was Defined.
def recommender(text):
    ratings = matrix[text]
    similar = matrix.corrwith(ratings).sort_values(ascending = False)
    similar = pd.DataFrame(similar,columns=['Correlation'])
    similar = similar.join(rating['Count of ratings'])
    return similar[(similar['Count of ratings']> 100) & 
                   similar['Correlation']>0.4].sort_values('Correlation').head(10)