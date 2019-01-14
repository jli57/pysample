from datetime import datetime, timezone

class Tweet:
  def __init__(self, tweet_data, field_names):
    d = tweet_data._json
    tweet = {}

    for field in field_names:

      if field == 'name':
        tweet[field] = d['user'][field]
      elif field == 'media_type':
        media_type = []
        try:
          media = d['entities']['media']
          for m in media:
            media_type.append(m["type"])
        except:
          media_type = []

        tweet[field] = media_type
      elif field == 'created_at':
        tweet[field] = self.format_date(d[field])
      else:
        tweet[field] = d[field]

    self.tweet = tweet

  # convert to pst (local time)
  def format_date(self, date_str):
    utc_date = datetime.strptime(date_str, '%a %b %d %H:%M:%S %z %Y')
    pst_date = utc_date.astimezone(tz=None)
    return pst_date.strftime('%a %b %d %H:%M:%S %z %Y')

