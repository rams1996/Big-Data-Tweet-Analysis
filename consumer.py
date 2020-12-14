import elasticsearch
import kafka
import json
import textblob

eskibana = elasticsearch.Elasticsearch(hosts=['localhost'], port=9200)


def main():
    consumer_subscription = kafka.KafkaConsumer("twitter_stream_corona_tweets", auto_offset_reset='earliest')
    
    def check_sentiment(polarity):
        tweet_sentiment = ""
        if polarity > 0:
            tweet_sentiment = 'POSITIVE'
        elif polarity < 0:
            tweet_sentiment = 'NEGATIVE'
        elif polarity == 0:
            tweet_sentiment = 'NEUTRAL'
        return tweet_sentiment
    for each_tweet in consumer_subscription:
        dict_data = json.loads(each_tweet.value)
        temp = textblob.TextBlob(dict_data["text"])
        polarity = textblob.TextBlob(dict_data["text"]).sentiment.polarity
        tweet_sentiment=check_sentiment(polarity)
        
        eskibana.index(
                    index="trump_tweets",
                    doc_type="test_doc",
                    body={
                    "author": dict_data["user"]["screen_name"],
                    "date": dict_data["created_at"],
                    "message": dict_data["text"],
                    "polarity": tweet_sentiment
                    }
                )
        print(str(temp))
        print('\n')


if __name__ == "__main__":
    main()
