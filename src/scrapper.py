from bs4 import BeautifulSoup
import urllib2
import io
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys   
from selenium.webdriver.common.by import By
import time
import codecs

def remove_html_tags(text):
        """Remove html tags from a string"""
        import re
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

#System.setProperty("webdriver.chrome.driver", "/home/rmartinez/reggaeton/chromedriver");
driver = webdriver.Chrome("/home/rmartinez/reggaetonsentiment/chromedriver")
driver.get("http://generourbano.com/reggaeton-top")

for i in range(0,300):
	search = driver.find_elements(By.XPATH,'//div')
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(1)
	driver.execute_script("window.scrollTo(0, 0);")
	time.sleep(1)
	if driver.find_elements_by_partial_link_text('CARGAR'):
		click = driver.find_elements_by_partial_link_text('CARGAR')
		for elem in click:
			elem.click()


linkList = []

for elem in search:
	if elem is not None and elem.get_attribute("href") is not None:
		linkList.append(elem.get_attribute("href"))

href = list(set(linkList))

for link in href:
	new_url = link
	try:
		new_page = urllib2.urlopen(new_url)
	except ValueError:
		continue

	new_soup = BeautifulSoup(new_page, 'lxml')

	content = new_soup.find_all('div', class_='track-content')

	if content:
		new2_soup = BeautifulSoup(str(content[0]), 'lxml')
		titles = new2_soup.find_all('h2')
		lyrics = new2_soup.find_all('p')
		title = remove_html_tags(str(titles[0]))
		space = ''
		lyricsJoined = space.join(str(lyrics))
		lyricsNoTags = remove_html_tags(lyricsJoined)
		with codecs.open('/home/rmartinez/reggaetonsentiment/canciones/songs.txt', 'a') as file:
			file.write(title + '\n')
			file.write(lyricsNoTags + '\n')


# url = 'http://www.generourbano.com'
# page = urllib2.urlopen(url)
# soup = BeautifulSoup(page, 'lxml')

# href = [link.get('href') for link in soup.find_all('a')]
# href = list(set(href))

# for link in href:
# 	new_url = link
# 	print(new_url)
# 	try:
# 		new_page = urllib2.urlopen(new_url)
# 	except ValueError:
# 		continue

# 	new_soup = BeautifulSoup(new_page, 'lxml')

# 	content = new_soup.find_all("div", class_="track-content")
# 	print(type(content))
# 	print(content)
# 	if content:
# 		new2_soup = BeautifulSoup(str(content[0]), 'lxml')
# 		titles = new2_soup.find_all("h2")
# 		lyrics = new2_soup.find_all("p")
# 		title = remove_html_tags(str(titles[0]))
# 		space = ''
# 		lyricsJoined = space.join(str(lyrics))
# 		lyricsNoTags = remove_html_tags(lyricsJoined)
# 		with io.FileIO("songs.txt", "a") as file:
# 			file.write(title + '\n')
# 			file.write(lyricsNoTags + '\n')






