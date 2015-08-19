from BeautifulSoup import BeautifulSoup

import argparse
import os
import urllib2
import urlparse

def download_episode(eps_link, subdir='', download_all=False, counter=0):
	actual_link = eps_link.strip('/')
	str_episode = 'chapter ' + str(counter) if download_all else actual_link.split('/')[-1]
	print ('Downloading chapter "' + str_episode + '"')

	html_page   = urllib2.urlopen(actual_link)
	soup        = BeautifulSoup(html_page)
	url_list    = [];
	for divs in soup.findAll('div', {"class" : "entry"}):
		for link in divs.findAll('img'):		
			url_list.append(link.get('src'))

	items_count = len(url_list)
	
	print "Got " + str(items_count) + " item(s) to download"

	counter = 1
	if items_count <= 0:
		print "No item to download"
	else:
		if not os.path.exists(subdir + str_episode):
			os.makedirs(subdir + str_episode)
		for i in range(0, len(url_list)):
			try:
				file_name = url_list[i].split('/')[-1]
				print "Downloading item " + str(i + 1) + " of " + str(items_count) + " (" + str_episode + "/page" + str(counter) + os.path.splitext(urlparse.urlparse(file_name).path)[1] + ")"
				image_data = urllib2.urlopen(url_list[i])
				out_file = open(subdir + str_episode + "/page" + str(counter) + os.path.splitext(urlparse.urlparse(file_name).path)[1], 'wb')
				out_file.write(image_data.read())
				out_file.close()			
				counter += 1
			except urllib2.HTTPError, error:
				pass

def download_all_episodes(manga_link):
	actual_link = manga_link.strip('/')
	html_page = urllib2.urlopen(actual_link)
	soup = BeautifulSoup(html_page)

	url_list = []
	for divs in soup.findAll('table'):
		for link in divs.findAll('a'):
			eps_link = link.get('href')
			if eps_link.find('mangaku.web.id') > 0:				
				url_list.append(eps_link)

	# sort episodes ascending
	url_list.reverse()

	dir_name = urlparse.urlparse(manga_link).path.replace('/', '')

	chap_counter = 1
	# begin download
	for url in url_list:		
		download_episode(url, dir_name + '/', True, chap_counter)
		chap_counter += 1

argument_parser = argparse.ArgumentParser(description = "Download either all chapters or a single chapter of a manga from mangaku.web.id.")
argument_parser.add_argument('-a', '--all', type=str, help = 'Download all chapters from a specified link')
argument_parser.add_argument('-s', '--single', type=str, help = 'Download a single chapter from a specified link')
args = argument_parser.parse_args()

if args.all and args.single:
	print "Please choose only one mode (either single or all)."
elif args.all:
	download_all_episodes(args.all)
elif args.single:
	download_episode(args.single)
else:
	argument_parser.print_help()