import os
import tweepy as tw
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

from textblob import TextBlob
from tweepy import OAuthHandler

# keys and tokens from the Twitter API console - make your own Twitter developer account and input your credentials
consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xxx'
access_token_secret = 'xxx'

# configure authentication and create tweepy API object to handle tweets

# low cost search words provided
low_cost_search = {"Southwest Airlines": "#southwestairlines", "Spirit Airlines": "#spiritairlines",
                   "JetBlue": "#jetblue", "Frontier Airlines": "frontier airlines", "Ryanair": "ryanair",
                   "easyJet": "easyjet", "AirAsia": "air asia", "Jetstar": "jetstar"}
# luxury search words provided
luxury_search = {"Singapore Airlines": "#singaporeair", "Etihad Airways": "etihad airways",
                 "Emirates": "emirates airline", "Cathay Pacific": "cathay pacific", "Qatar Airways": "qatar airways",
                 "Japan Airlines": "japan airlines", "Lufthansa": "lufthansa", "Air France": "air france"}

# change your date that your queried tweets start - a week before you are running your project is a good date
date_since = "2019-09-12"
# for this project, data on positive, neutral and negative sentiment will be collected.

# create a dataframe with an index keeping track of those three categories
"""
Insert your dataframe code here
"""

"""
Given a search dictionary (low_cost_search or luxury_search) and the number of tweets desired, this function mines the 
Twitter API for 'num_tweets' tweets with the search query from the values of the given dictionary. For each tweet, it 
then determines whether it has positive, neutral or negative sentiment and keeps track of the number of tweets for each 
sentiment category. Then a row is added to the dataframe with the label from the dictionary key related to that search 
query, and the positive, neutral and negative values gathered. This dataframe is compiled and then returned. The result
returned should be a dataframe that contains the number of positive, neutral and negative tweets for each airline 
related to an airline category (low-cost or luxury in this case).
"""
def produce_dataframe(search_dict, num_tweets):
    return 'TO-DO'


"""
Initializes two dataframes - one for low_cost_search and one for luxury_search - using the produce_dataframe function.
The number of tweets gathered should be 100. Print the dataframes to the Python console and then return both of them.
Bear in mind mining 100 tweets will take a while, please be patient.
"""
def init_dataframes():
    return 'TO-DO'


"""
Based on the p-values and t-statistics from the two tests, comes to a conclusion regarding the data.
First check if the null hypothesis can be rejected and if so, the correct alternative hypothesis.
Use a significance level of 0.10.
Hint: check the p-value first and then the sign of the t-statistic.
"""
def conclusion(pos_p, neg_p, pos_t, neg_t):
    # Bear in mind the methods we have studied test for two-tailed equality. How can we make a two-tailed test testing equality into a one-tailed test testing comparison?
    # Use a significance level of 0.10
    return "TO-DO"


"""
The code under this comment block will be executed directly.
You should do four things here:
1) Initialize two dataframes pertaining to low cost and luxury airlines using init_dataframes() and produce_dataframe()
2) Conduct two two-tailed T-tests to check whether the positive and negative sentiments are equal.
3) Print your t-statistics and p-values to the console (please label them!)
4) Come to a conclusion (conclusion() method) regarding the data. Conclusions should be printed to the console.
"""

"""
Insert your main code here
"""

