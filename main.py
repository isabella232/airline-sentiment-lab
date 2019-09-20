import os
import tweepy as tw
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

from textblob import TextBlob
# keys and tokens from the Twitter Dev Console
from tweepy import OAuthHandler

consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xxx'
access_token_secret = 'xxx'
# attempt authentication
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tw.API(auth, wait_on_rate_limit=True)

# low cost search words
low_cost_search = {"Southwest Airlines": "#southwestairlines", "Spirit Airlines": "#spiritairlines",
                   "JetBlue": "#jetblue", "Frontier Airlines": "frontier airlines", "Ryanair": "ryanair",
                   "easyJet": "easyjet", "AirAsia": "air asia", "Jetstar": "jetstar"}
# luxury search words
luxury_search = {"Singapore Airlines": "#singaporeair", "Etihad Airways": "etihad airways",
                 "Emirates": "emirates airline", "Cathay Pacific": "cathay pacific", "Qatar Airways": "qatar airways",
                 "Japan Airlines": "japan airlines", "Lufthansa": "lufthansa", "Air France": "air france"}
date_since = "2019-09-12"
df = pd.DataFrame([], index=['positive', 'neutral', 'negative'])


def produce_dataframe(search_dict, num_tweets):
    df = pd.DataFrame([], index=['positive', 'neutral', 'negative'])
    for key, val in search_dict.items():
        # Collect tweets
        tweets = tw.Cursor(api.search,
                           q=val,
                           lang="en",
                           since=date_since).items(num_tweets)
        positive = 0
        neutral = 0
        negative = 0
        for t in tweets:
            analysis = TextBlob(t.text)
            if analysis.sentiment.polarity > 0:
                positive += 1
            elif analysis.sentiment.polarity == 0:
                neutral += 1
            else:
                negative += 1
        df[key] = [positive, neutral, negative]
    return df


def init_dataframes():
    low_cost_df = produce_dataframe(low_cost_search, 100)
    luxury_cost_df = produce_dataframe(luxury_search, 100)
    print(low_cost_df.to_string())
    print(luxury_cost_df.to_string())
    return low_cost_df, luxury_cost_df


def conclusion(pos_p, neg_p, pos_t, neg_t):
    """
    Because stats.ttest_Ind(a, b) tests for two-tailed equality, we can convert this test to a one-tailed test by dividing the p-value by 2.
    If we are testing if a > b, then our null hypothesis would be b <= a and our alternative is a > b.
    We can only reject the null hypothesis if p/2 < alpha, which indicates our results are too extreme under the assumption the null hypothesis is true
    and accounting for the fact that our test has to be one-tailed due to the one-sided greater than premise.
    Additionally, t has to be greater than zero, otherwise b > a.
    If the t-statistic ends up being negative and p/2 < alpha, then it can be concluded b > a.
    """

    # significance level of 0.10
    if pos_p / 2 < 0.10:
        if pos_t > 0:
            print("Low cost airlines have more positive sentiment than luxury airlines.")
        else:
            print("Luxury airlines have more positive sentiment than low cost airlines.")
    else:
        print("No conclusion can be made about positive sentiment.")

    if neg_p / 2 < 0.10:
        if neg_t > 0:
            print("Low cost airlines have more negative sentiment than luxury airlines.")
        else:
            print("Luxury airlines have more negative sentiment than low cost airlines.")
    else:
        print("No conclusion can be made about negative sentiment.")


low_df, luxury_df = init_dataframes()
# 2-tailed T-test: positive sentiment for low-cost = positive sentiment for luxury
pos_t_stat, pos_p_value = stats.ttest_ind(low_df.loc['positive'], luxury_df.loc['positive'])
# 2-tailed T-test: negative sentiment for low-cost = negative sentiment for luxury
neg_t_stat, neg_p_value = stats.ttest_ind(low_df.loc['negative'], luxury_df.loc['negative'])

print(f"Positive t-statistic: {pos_t_stat}")
print(f"Positive p-value: {pos_p_value}")
print(f"Negative t-statistic: {neg_t_stat}")
print(f"Negative p-value: {neg_p_value}")

conclusion(pos_p_value, neg_p_value, pos_t_stat, neg_t_stat)
