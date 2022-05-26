import pandas as pd
import snscrape.modules.twitter as sntwitter

query = "(#gdańsk AND #covid) until:2022-02-15 since:2020-12-20"
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
