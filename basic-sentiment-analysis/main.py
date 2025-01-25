import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime
import logging
import os


def setup():
    # datetime object containing current date and time
    now = datetime.now()
    datetime_string = now.strftime("%Y%m%d-%H%M%S")
    env = os.getenv('ENVIRONMENT')

    logging.basicConfig(filename='./logs/crawler-{}-{}.log'.format(datetime_string, env), encoding='utf-8', level=logging.DEBUG)



# reading and wrangling data
csv_path = os.getenv('CSV_PATH', '/app/data/avatar.csv')
field_name = os.getenv('FIELD_NAME', 'character_words')

df_avatar = pd.read_csv(csv_path, encoding='unicode_escape', engine='python')
df_character_sentiment = df_avatar[df_avatar[field_name].str.len() >= 1]

# calculating sentiment score
sid = SentimentIntensityAnalyzer()
df_character_sentiment.reset_index(inplace=True, drop=True)
print(df_character_sentiment)
df_character_sentiment[['neg', 'neu', 'pos', 'compound']] = df_character_sentiment[field_name].apply(sid.polarity_scores).apply(pd.Series)
print(df_character_sentiment)
