#Question 1
print("Question 1")
print("An access token is an object that describes "
      "the security context of a process or thread."
      " The information in a token includes the identity"
      " and privileges of the user account associated with"
      " the process or thread. ... The security identifier"
      " (SID) for the user's account. SIDs for the groups"
      " of which the user is a member.")
#Question 2
print("Question 2")
print("IP Address of google.com:   172.217.161.14")
print("IP Address of facebook.com:  157.240.23.35")
#Question 3
print("Question 3")
import tweepy
CONSUMER_KEY = 'ohDQtO0FFgJwz7dp318YO3gmT'
CONSUMER_SECRET = 'G8ayK8oUrgzW7vNIJsUG5b6duKILhRt8NuVyq5J9D3rfDMmQux'
ACCESS_TOKEN = '1006836320855998464-xva0bH9SLCp5bWqXitoS9gVN1E8TYB'
ACCESS_TOKEN_SECRET = 'Q5TMBRkYW1ttc8prDrVU03ZGAz4ALnel5PPDSYj2cBhyk'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
status = "Hello"
api.update_status(status=status)
#Question 4
print("Question 4")
print("A Library is a chunk of code that you can call from your own code, to help you do things more quickly/easily. For example, a Bitmap Processing library will provide facilities for loading and manipulating bitmap images, saving you having to write all that code for yourself. Typically a library will only offer one area of functionality (processing images or operating on zip files)"
      "An API (application programming interface) is a term meaning the functions/methods in a library that you can call to ask it to do things for you - the interface to the library.")
#Question 5
print("Question 5")
