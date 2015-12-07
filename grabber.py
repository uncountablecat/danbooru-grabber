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
def grabber(tag_argv,page_num):
	r = requests.get('https://danbooru.donmai.us/posts.json?tags='+tag_argv+'&page='+str(page_num))
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


def main():
	page_num = input('Enter the number of pages you want to download. To download all, simply enter a super large number:')
	taginput = raw_input('Enter tags,separated by space:') 

	n = 1
	while n <= page_num:
		tagList = taginput.split(' ')
		tag_argv = generate_tag_argv(tagList)
		grabber(tag_argv,n)
		n = n + 1

	tagList = tagList.split(' ')
	tag_argv = generate_tag_argv(tagList)
	grabber(tag_argv,pic_num)


	print('Download successful!')
	u2 = u'どうぞ、召し上がってください！'
	print u2


if __name__ == '__main__':
	main()