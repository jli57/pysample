import json
from src.tweet_mananger import TweetManager
from src.file_handler import FileHandler
import src.teams

def initialize():
    ''' This is a function that prints Hello World to the console
    '''
    # get keys
    with open('keys.json') as f:
      data = json.load(f)

    print("Starting...")

    # inititalize TweetManager
    t = TweetManager(data)

    field_names = [ 'id', 'name', 'created_at', 'text', 'media_type']

    data = t.get_all_tweets( src.teams.nfl, field_names )
    f = FileHandler(data, field_names)

    print("Finished")


if __name__ == '__main__':
    # Entry point for command
    initialize()
