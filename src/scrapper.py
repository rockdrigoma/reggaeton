from bs4 import BeautifulSoup
import urllib2
import io
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys   
from selenium.webdriver.common.by import By
import time 

def remove_html_tags(text):
        """Remove html tags from a string"""
        import re
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

url = 'http://www.generourbano.com'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'lxml')

href = [link.get('href') for link in soup.find_all('a')]
href = list(set(href))

for link in href:
	new_url = link
	print(new_url)
	try:
		new_page = urllib2.urlopen(new_url)
	except ValueError:
		continue

	new_soup = BeautifulSoup(new_page, 'lxml')

	content = new_soup.find_all("div", class_="track-content")
	print(type(content))
	print(content)
	if content:
		new2_soup = BeautifulSoup(str(content[0]), 'lxml')
		titles = new2_soup.find_all("h2")
		lyrics = new2_soup.find_all("p")
		title = remove_html_tags(str(titles[0]))
		space = ''
		lyricsJoined = space.join(str(lyrics))
		lyricsNoTags = remove_html_tags(lyricsJoined)
		with io.FileIO("songs.txt", "a") as file:
			file.write(title + '\n')
			file.write(lyricsNoTags + '\n')






