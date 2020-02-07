
import tweepy as tp
import time
# credentials to login to twitter ap
consumer_key = '4RYCTuQcj3T4QvrgBqcAOMXKn'
consumer_secret = 'PPVmrZq8Wjbwh5lHKxclTpmNReMESipEHYaxL61ApKYsiNstrf'
access_token = '1225651180115677184-piBnM2AyURQNlFVOIo7tw3HGE0scCu'
access_secret = 'Vsc5zXWVbnta1wv1bnFDwR8qn8ihZvM8Avb1ZsaAtTB9h'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)



# update status
for api.update_status("i love you, ❤️!")
    time.sleep(3)
