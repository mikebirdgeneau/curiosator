from twitter import *
from secrets import *
import psycopg2

#t = Twitter(
#    auth=OAuth(secrets.access_key_token, secrets.access_token_secret,
#               secrets.app_key, secrets.app_secret))
#t.statuses.home_timeline()

twitter_stream = TwitterStream(
    auth=OAuth(access_key_token, access_token_secret, app_key, app_secret),
    domain='stream.twitter.com'
)

print("Connecting to stream...")
iterator = twitter_stream.statuses.filter(track="oil price, shale gas, oil sands")
count = 0
for twt in iterator:
    #if twt['entities']['urls'].__len__ > 0:
    urls = twt['entities']['urls']
    print(twt)
    print(twt['id_str'])
    print(twt['timestamp_ms'])
    print(twt['text'])
    print[twt['user']['screen_name']]
    print(twt['user']['followers_count'])
    for u in urls:
        print(u['expanded_url'])
    count += 1
    if count >= 100:
        break

print("Done.")