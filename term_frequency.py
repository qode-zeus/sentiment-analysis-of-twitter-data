import sys
import json
import operator
def main(tweetfile):
  tweet_file = open(tweetfile)                      
  tweet_hash = {}                                     
  for tweet_line in tweet_file:                       
    tweet = json.loads(tweet_line)                    
    if "entities" in tweet.keys():                   
      hashtags = tweet["entities"]["hashtags"]       
      for ht in hashtags:                            
        if ht != None:                                
          if ht["text"].encode("utf-8") in tweet_hash.keys():  
            tweet_hash[ht["text"].encode("utf-8")] += 1        
          else:
            tweet_hash[ht["text"].encode("utf-8")] = 1         
 
  sortedHashTags = dict(sorted(tweet_hash.items(), key=operator.itemgetter(1), reverse=True)[:10])  
                                                                                                  
  print("HashTag Name   -   Frequency\n\n")                                                        
  for key,value in sorted(sortedHashTags.items(), key=lambda kv: (kv[1],kv[0]),reverse=True):     
    print("#%s -  %d" % (key.decode("utf-8"), value))                                             

    
if __name__ == '__main__':
  if len(sys.argv) == 2:
    main(sys.argv[1])
  else:
    print('Usage: give the filename containing your tweets as argument')
 
