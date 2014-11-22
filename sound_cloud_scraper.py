# Filename: sound_cloud_scraper.py
# Author: Justine Lee
# Date: 10.5.2014 
# Description: program for scraping SoundCloud for urls of cover songs

import urllib2
import time
from selenium import webdriver

# Given the song name and artist will return a list of 
def get_cover_urls(song, artist):
	query = song + artist + " COVER"
	search_url = "http://soundcloud.com/search/sounds?q=" + urllib2.quote(query)
	
	driver = webdriver.Firefox()
	driver.implicitly_wait(30) # seconds

	# Scroll down page three times
	driver.get(search_url)
	time.sleep(5)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(5)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	# Find all elements with 
	elements = driver.find_elements_by_class_name("sc-media-content")
	cover_urls = []

	contains = song.split(" ") + artist.split(" ") + ["COVER"]

	for elem in elements:
		add_to_list = True 

		link = elem.find_element_by_css_selector("a").get_attribute("href")
		link = link.upper()

		for term in contains:
			if not term.strip() in link:
				add_to_list = False
		
		if add_to_list:
			cover_urls.append(link)

	time.sleep(5)

	driver.quit()

	return cover_urls

# Given the filename of the file containing songs to be scraped will 
# write out urls of found SoundCloud covers into another given file
def main(song_filename,url_filename):
	# Open the files for reading and writing
	song_file = open(song_filename,'r')
	url_file = open(url_filename,'w')

	search_urls = []
	url_dictionary = {}

	#Read in songs line by line
	for line in song_file:
		line = line.strip()
		song_info = line.split("~")
		url_dictionary[line] = get_cover_urls(song_info[0],song_info[1])
		print line
		print url_dictionary[line]
		print

	for line in url_dictionary:
		url_file.write(line+"\n")
		for url in url_dictionary[line]:
			url_file.write(url.lower().replace("https","http")+"\n")
		url_file.write("\n")

	# Close the files
	song_file.close()
	url_file.close()

main('songs.txt','cover_urls_lower.txt')
