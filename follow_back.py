"""
This script is going to check and follow back all Marvin's followers
"""

from secret_keys import *
from wiki_random import *
from random import seed
from random import randint
from time import sleep
import tweepy
import time
import csv

def check_csv():
	file = "my_followers.csv"
	try:
		with open(file, mode = 'r') as csv_file:
			csv_file.close()
			return True
	except Exception:
		with open(file, mode = 'w') as csv_file:
			main_row = csv.writer(csv_file, delimiter = ';', lineterminator = '\n', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
			main_row.writerow(['Follower', 'ID'])
		csv_file.close()
		print("CSV file has been created\n")

def add_followers(ap):
	controle = False
	check_csv()
	users = tweepy.Cursor(ap.followers).items()
	for user in users:
		if check_follower(user.screen_name, user.id_str):
			continue
		user.follow()

		hello = RandomHello()
		wiki_page = RandomPhrase()
		msg = hello + '@' + user.screen_name + wiki_page
		print(msg)
		ap.update_status(msg)

		file = "my_followers.csv"
		friend_name = '@' + str(user.screen_name)
		friend_id = str(user.id_str)
		with open(file, mode = 'a') as csv_file:
			row = csv.writer(csv_file, delimiter = ';', lineterminator = '\n', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
			row.writerows([[friend_name, friend_id]])
			controle = True
		csv_file.close()
	if controle:
		print("All users has been add in your csv file!\n:)\n")
	else:
		print("No new followers!\n:(\n")


def check_follower(friend_name, friend_id):
	file = "my_followers.csv"
	with open(file, mode = 'r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=';')
		for row in csv_reader:
			try:
				if row[0] == ('@' + friend_name) and row[1] == friend_id:
					csv_file.close()
					return True
			except Exception:
				continue
		csv_file.close()
		return False
			
def RandomHello():
	msgs = ["Eae, ", "Olá, ", "Salve, ", "Beleza, ", "Oi, ", "Tranquilo(a), ", 
	       "Saudações, ", "Bem-vindo(a), ", "Opa, ", "Fala, "]
	num = randint(0, len(msgs))
	return msgs[num]

def RandomPhrase():
	msgs = ["! Toma este artigo sobre ", "! Fica com este artigo sobre ", "! Fica com esta página sobre ", 
	       "! Saindo uma página fresquinha de ", "! Mais um aleatório sobre ", "! Escolhido especialmente pra você sobre ",
	       "! Duvido você ler tudo sobre ", "! Que tal ler sobre "]
	num = randint(0, len(msgs))
	infos = AccessHTML()
	phrase = msgs[num] + "'" + infos[1] + "' :\n"+ infos[0]
	return phrase

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_secret_token)
api = tweepy.API(auth)

seed()
while True:
	try:
		add_followers(api)
	except tweepy.TweepError:
		print("Sleeping for 15 minutes. . .\n")
		time.sleep(60*15)
		continue
	except KeyboardInterrupt:
		break
