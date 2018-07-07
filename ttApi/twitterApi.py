from twython import Twython

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

def search(ticker):
    return twitter.search(q=ticker,result_type='recent', lang='en', count=100)