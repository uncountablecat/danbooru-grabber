#!/usr/bin/python
#coding:utf-8
import os # path manipulation
import urllib as urllib
import requests

# change this to your danbooru folder
# it might look something like this: '/users/YourUserName/DanbooruPics'
# make sure the folder already exists!
danbooru_folder = '/Users/chaoguo/gelboorupics/'

# generate tag argument to be used in url and folder creation
def generate_tag_argv(tagList):
	tag_argv = ''
	for tag in tagList:
		tag_argv = tag_argv + tag + '+'
	tag_argv = tag_argv[:-1]

	return tag_argv

# request json, get urls of pictures and download them
def grabber(tag_argv,pic_num):
	r = requests.get('https://danbooru.donmai.us/posts.json?tags='+tag_argv+'&limit='+str(pic_num))
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

pic_num = input('Enter the number of posts you would like to download:')
while (pic_num >100):
	print('The number is not valid!')
	print('Danbooru only allows 100 pictures at most!')
	u1 = u'健全な生活を送りましょう！'
	print u1
	pic_num = input('Enter the number of posts you would like to download:')

tagList = raw_input('Enter tags,separated by space:') 
tagList = tagList.split(' ')
tag_argv = generate_tag_argv(tagList)
grabber(tag_argv,pic_num)

print('Download successful!')
u2 = u'どうぞ、召し上がってください！'
print u2