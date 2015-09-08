from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
# Obtain credentials from twitter
ckey='enter your consumer key'
csecret='enter your consumer secret'
atoken='enter your access token'
asecret='enter yout access secret'
class listener(StreamListener):
        def on_data(self,data):
                try:
                        print(data)                    
                except:
                        print(" ")
                return True
        def on_error(self,status):
                print(status)
                return True
        
auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
TwitterStream = Stream(auth,listener())
TwitterStream.filter(track=["hacker"])	

# use this command to load all your tweets into a file "python tweet_collector.py > filename.json"
