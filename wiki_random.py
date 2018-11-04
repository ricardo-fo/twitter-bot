from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import requests

def ErrorTest(URL):
	try:
		html = urlopen(URL)
	except HTTPError as err:
		print(err)
		return None
	except URLError:
		print("Server down or incorrect domain!\n")
		return None
	except Exception:
		return None
	else:
		return URL

def AccessHTML():
	URL = ErrorTest("https://pt.wikipedia.org/wiki/Especial:Aleat%C3%B3ria")
	if URL == None:
		print("Unfortunally, this web site is inaccessible\n:(\n")
		return 1
	page = requests.get(URL, timeout = 5)
	soup = BeautifulSoup(page.content, "html5lib")
	page.close()
	link = GetLink(soup)
	#print(link)
	title = GetTitle(soup)
	#print(title)
	return [link, title]


def GetLink(parse):
	general = parse.find("link", attrs = {"rel":"canonical"})
	return general.get('href')

def GetTitle(parse):
	general = parse.find("title").text
	return general[:len(general)-34]
