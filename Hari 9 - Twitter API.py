# import library
import pandas as pd
import tweepy
import re

# persiapkan key
token_data = pd.read_csv('key.csv')

keys=[]
for i in token_data:
    keys.append(token_data[i][0])

consumer_key = keys[0]
consumer_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]

# buat handler untuk auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# scraping tweet
user = "jokowi"
counts = 100
timeline = api.user_timeline(id=user, count=counts, tweet_mode='extended')

tweet = []
for i in timeline:
    tweet.append(i.full_text)

# membuat dataframe
df = pd.DataFrame()
df['tweet'] = tweet

# text cleaning
remove = re.compile(r'\n\n|http\S+')
df['tweet'] = [remove.sub('', i) for i in df['tweet']]

# mencari keyword dan indexing
keyword = 'Covid'

idx = []
for i, j in enumerate(df['tweet']):
    if re.search(keyword, j):
        idx.append(i)

# indexing dengan keyword yang sesuai
df_filtered = df['tweet'].iloc[idx]

# print hasil
print('banyaknya tweet pak Jokowi yang diambil :', len(df))
print('banyaknya pak Jokowi membicarakan Covid dalam tweetnya :', len(df_filtered))