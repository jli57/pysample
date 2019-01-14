import csv
import json
from .text_formatter import replace_text

class FileHandler:
  def __init__(self, tweets, field_names, csvPath = "results.csv", jsonPath = "results.json"):
    self.csvPath = csvPath
    self.jsonPath = jsonPath
    self.field_names = field_names
    self.create_csv_file(tweets)
    self.create_json_file

  # create csv file
  def create_csv_file( self, tweets ):
    with open( self.csvPath, 'w', newline='') as csv_file:
      writer = csv.DictWriter( csv_file, fieldnames=self.field_names)
      writer.writeheader()
      for tweet in tweets:
        writer.writerow(tweet)

  # open csv file and process data
  def process_csv_data( self ):
    data = []

    with open( self.csvPath ) as csv_file:
      csv_reader = csv.reader( csv_file, delimiter=',')
      line_count = 0
      headers = []
      # for each tweet
      for row in csv_reader:
        # each tweet
        tweet = {}
        if line_count == 0:

          headers = row
        else:
          # write each column in the row as a json key-value pair
          for i, col in enumerate(row):
            # replace coach, superbowl, and playoff with GreenPark
            if headers[i] == 'text':
              col = replace_text(col)
            tweet[headers[i]] = col
          # add to data
          data.append(tweet)
        line_count += 1
    return data

  # write to json
  def create_json_file( self ):
    data = self.process_csv_data
    with open(self.jsonPath, 'w') as json_file:
      json.dump(data, json_file)
