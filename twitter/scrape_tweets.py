import json
from langdetect import detect
from snscrape.modules import twitter
import csv_reader
import get_dates

keywords = csv_reader.get_random_keywords('keywords.csv', 'keywords', 3)

print(keywords)

negative_words = csv_reader.get_all_keywords('negative_keywords.csv', 'keywords')

print(negative_words)

date_from, date_to = get_dates.get_dates(2)

print(date_from + '  ' + date_to)

start = date_from
end = date_to

max_num = 5000
languages = 'en'

reply_count = 10
followers_count = 100000
like_count = 100
retweet_count = 1

file_name = 'tweet.json'

open(file_name, 'w', encoding='utf-8')

for keyword in keywords:
    for i, tweet in enumerate (twitter.TwitterSearchScraper(f'{keyword} + since:{start} until:{end}').get_items()):
        try:
            lan = detect(tweet.content)
        except:
            lan = 'error'
        if i >= max_num:
            break
        if lan in languages:
            data = {'id': tweet.id, 'username': tweet.username, 'user': tweet.user,
                    'followers': tweet.user.followersCount, 'date': tweet.date,
                    'url': tweet.url, 'likes': tweet.likeCount, 'replys': tweet.replyCount,
                    'retweets': tweet.retweetCount, 'quoteCount': tweet.quoteCount, 'text': tweet.content}
            if tweet.replyCount >= reply_count:
                if tweet.user.followersCount >= followers_count:
                    if tweet.likeCount >= like_count:
                        if tweet.retweetCount >= retweet_count:
                            list_str = tweet.content
                            my_list = [list_str]
                            matching = [s for s in my_list if any(xs in s for xs in keywords)]
                            if not matching:
                                with open(file_name, 'a+', encoding='utf-8') as f:
                                    line = json.dumps(data, ensure_ascii=False, default=str)
                                    f.write(line)
                                    f.write('\n')
print('Done!!')
