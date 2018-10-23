"""
INI: 22/10/2018
This is a project to make a bot. I'm not sure what I going to do, but
this is gonna be a Twitter bot. Please, check it on official Twitter bot 
account: https://twitter.com/MarvinOAndroid1
You're free to use and modify the source code

Author: Ricardo Freitas
Github: github.com/ricardo-fo
Twitter: https://twitter.com/RicardoFoo__
"""
import tweepy
import tkinter
import csv

#Main loop
def main_loop(ap):
	follow_back(ap)
	post_tweet(ap)


#Follow every followers back
def follow_back(ap):
	for follower in tweepy.Cursor(ap.followers).items():
		if check_follower(follower.screen_name, '@' + str(follower.screen_name)):
			print("Following: @", follower.screen_name)
			continue
		follower.follow()
		ap.update_status("Hello, my new friend @" + follower.screen_name)
		print("New friend: @" + follower.screen_name)

#Post a tweet
def post_tweet(ap):
	with open("time.txt", "r") as file:
		for line in file:
			ap.update_status(line)
			break
	file.close()
	print("Tweeted successfully!")

#Check if I have new followers
def check_follower(friend_name, friend_id):
	filename = 'my_followers.csv'
	fields = []
	with open(filename, 'r') as csvfile:
		csvreader = csv.reader(csvfile, delimiter = ',')
		for row in csvreader:
			if len(row) == 0:
				continue
			if row[0] == friend_name and row[1] == friend_id:
				return True
	csvfile.close()

	new = [[friend_name, friend_id]]
	with open(filename, 'a') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerows(new)
	csvfile.close()
	return False

#Credentials
consumer_key = "ENTER HERE YOUR CONSUMER KEY"
consumer_secret = "ENTER HERE YOUR CONSUMER SECRET KEY"
access_token = "ENTER HERE YOUR ACCESS TOKEN"
access_token_secret = "ENTER HERE YOUR ACCESS SECRET TOKEN"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while main_loop(api):
	pass