import pandas as pd
import snscrape.modules.twitter as sntwitter

query = "League of legends"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query=query).get_items():
    print(vars(tweet))
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'user', 'Tweet'])

print(df)
