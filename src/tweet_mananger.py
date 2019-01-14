import tweepy
from .tweet import Tweet

class TweetManager:

  def __init__(self, keys):

    # initialize auth
    auth = tweepy.OAuthHandler(keys["CONSUMER_KEY"], keys["CONSUMER_SECRET"])
    auth.set_access_token(keys["ACCESS_TOKEN"], keys["ACCESS_SECRET"])

    # define api
    self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


  def get_all_tweets(self, names, field_names, num = 20):

    all_tweets = []
    # for each team
    for n in names:

      print(f'Retriving tweets for {n}...')
      # get tweets
      tweets = self.get_tweets( n, num )

      # if there request is successful
      if tweets:
        # format tweet
        for tweet in tweets:
          t = Tweet(tweet, field_names)

          all_tweets.append(t.tweet)

    return all_tweets

  # make a call to get tweets
  # do error handling here
  def get_tweets(self, name, num = 20):
    try:
      tweets = self.api.user_timeline(screen_name=name, count=num)
      return tweets
    except tweepy.TweepError as e:
      # return empty list if tweets cannot be returned
      print(f'Could not retrieve data for {name}')
      print(e)
      return []

