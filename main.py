import asyncio
from twikit import Client, TooManyRequests
import time
from datetime import datetime
import csv
from configparser import ConfigParser
from random import randint

MINIMUM_TWEETS = 500
QUERY = 'when we were young'

async def get_tweets(tweets):
    if tweets is None:
        print(f'{datetime.now()} - Getting tweets...')
        tweets = await client.search_tweet(QUERY, product='Latest')  
    else:
        wait_time = randint(5, 10)
        print(f'{datetime.now()} - Getting next tweets after {wait_time} seconds ...')
        await asyncio.sleep(wait_time)  
        tweets = await tweets.next()  

    return tweets

# load credentials
async def main():
    config = ConfigParser()
    config.read('config.ini')
    username = config['X']['username']
    email = config['X']['email']
    password = config['X']['password']

    with open('tweets_when_wwy.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Tweet ID', 'Tweet_count', 'Username', 'Text', 'Created At', 'Retweets', 'Likes'])  # Adicionando 'Tweet ID' ao cabeçalho

    # authenticate to X
    global client
    client = Client(language='en-US')
    await client.login(auth_info_1=username, auth_info_2=email, password=password)

    tweet_count = 0
    tweets = None
    tweet_ids = set()  # manter controle dos ids unicos

    while tweet_count < MINIMUM_TWEETS:
        try:
            tweets = await get_tweets(tweets)
        except TooManyRequests as e:
            rate_limit_reset = datetime.fromtimestamp(e.rate_limit_reset)
            print(f'{datetime.now()} - Rate limit reached. Waiting until {rate_limit_reset}')
            wait_time = rate_limit_reset - datetime.now()
            await asyncio.sleep(wait_time.total_seconds())  
            continue

        if not tweets:
            print(f'{datetime.now()} - No more tweets found')
            break

        for tweet in tweets:
            if tweet.id in tweet_ids:  # verificar se o tweet já foi salvo
                continue

            tweet_ids.add(tweet.id)  
            tweet_count += 1
            tweet_data = [
                tweet.id,
                tweet_count,
                tweet.user.name,
                tweet.text,
                tweet.created_at,
                tweet.retweet_count,
                tweet.favorite_count
            ]
            
            # salvando os dados em csv
            with open('tweets_when_wwy.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(tweet_data)

        print(f'{datetime.now()} - Got {tweet_count} tweets')

    print(f'{datetime.now()} - Done! Got {tweet_count} tweets found')

if __name__ == '__main__':
    asyncio.run(main())
