
import kafka
import json
import tweepy

class KafkaPushListener(tweepy.streaming.StreamListener):
    def __init__(self):
        self.producer = kafka.KafkaProducer(bootstrap_servers=['localhost:9092'])

    def on_data(self, data):
        self.producer.send("twitter_stream_corona_tweets", data.encode('utf-8'))
        print(data)
        return True

    def on_error(self, status):
        print(status)
        return True

tweepy_token = tweepy.OAuthHandler("Tba4dz6iAhJ8aIlruIVyOgv1H", "hrMWxGtZPKjDPhWz6iPVRIXnrJAFofRqW8cCh3lQG9TKXSNUEs")  #Arguments are consumer key and consumer secret for authentication
tweepy_token.set_access_token("1250167730981998592-RVTbFdCcrbvxl4VWOPh1MMrur0Co0w", "n5K7kaJDMtMChQBqoMtPX957NJNdOyj1nY1O9Kapv5vZk") #Arguments are Access token and access secret for authentication
api = tweepy.API(tweepy_token)
tweepy.Stream(tweepy_token, KafkaPushListener()).filter(track=["#trump"])
