#!/usr/bin/python
#coding:utf-8
import os # path manipulation
import urllib as urllib
import requests

# change this to your danbooru folder
# it might look something like this: '/users/YourUserName/GelbooruPics'
# make sure the folder already exists!
danbooru_folder = '/users/NicoNicoNi/danboorupics/'

# generate tag argument to be used in url and folder creation
def generate_tag_argv(tagList):
	tag_argv = ''
	for tag in tagList:
		tag_argv = tag_argv + tag + '+'
	tag_argv = tag_argv[:-1]

	return tag_argv

# request json, get urls of pictures and download them
def grabber(tag_argv):
	r = requests.get('https://danbooru.donmai.us/posts.json?tags='+tag_argv+'&limit=60')
	streams = r.json()

	# check if directory already exists
	if (os.path.exists(danbooru_folder+tag_argv) == False):
		os.mkdir(danbooru_folder+tag_argv)

	url = []
	for post in streams:
		if 'file_url' in post:
			url.append(post['file_url'])
			target = ['https://danbooru.donmai.us'+x for x in url]

	# download
	for address in target:
		urllib.urlretrieve(address,danbooru_folder+tag_argv+'/'+address.split('/')[-1])

# you can use input instead of raw_input if you are using Python 3
tagList = raw_input('Enter tags,separated by space:') 
tagList = tagList.split(' ')
tag_argv = generate_tag_argv(tagList)
grabber(tag_argv)
print('Download successful!')
u = u'召し上がってください！'
print u