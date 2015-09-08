from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
ckey='zdKeglVccs3FPAaJIynm5AC0N'
csecret='e5zHsXTC245e5vKRXrLxCrB8BUIpwCRNq3lFiBvrYieKHnI4YK'
atoken='2921267035-M1wKR8bdOCqqgE5XYVnDDnxDHKdkkjaJvOEHg4A'
asecret='l3UIq1NAx3TVLuzBNRADKvtu3HBo9hWkqfYRIqt2gU6xd'
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
