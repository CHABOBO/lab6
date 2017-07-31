import tweepy

consumer_key = "iUzHPMpOvAJNeEa5jp6vds0E5 ";

consumer_secret = "tpbwZPRrjbadpMgt9g4ZwduoPPLTBqhNDbaIntNh3ojQbWjTbq";

access_token = "891521859723964416-7bzLSYEWiKbVMXTH0vgHhL9IjCl7JZ7";

access_token_secret = "	fBcajehMr1qOQN5wJaoMfG3jss3zcU7p0U91YpiyebQOG";

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



