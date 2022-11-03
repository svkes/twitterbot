import tweepy
import time

bearer_token = "AAAAAAAAAAAAAAAAAAAAAB7%2FggEAAAAALjy82J3pCoX%2Fo1nXtjyD0sDCOGs%3Ds0xPb3jVl9uP6kREKjzA2b0XR6ce1bN57tpdu0rUPlnZ3KVbHW"
access_token = "1566771454242197505-smHVWMSaHNYsxCfdi1MiD6qdZYPWRd"
access_secret = "TjioP6LFIOCFC09wr40keGhgrVUOInc8WolI3sfMw3Q7r"
api_key = "lUFp593FkPA3TjehSA6ONvk9M"
api_secret = "VccRMsK1m3LuFezelgwnXCQldb7LNexoE6V4NgcWRoPWAI6FR6"


auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return 


# ID: 1567287731222618113
def reply_to_tweets():
    print('retrieving and replying to tweets...')
    
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(since_id = last_seen_id)



    for mention in reversed(mentions):
        print(str(mention.id) + '-' + mention.text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if mention.author.id == 1566771454242197505:
            continue
        elif '#helloworld' in mention.text.lower():
            print('found #helloworld')
            print('responding back...')

            api.update_status(status = '@' + mention.user.screen_name + 
                    ' #HelloWorld back to you! ', in_reply_to_status_id = mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)