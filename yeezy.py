# imports
from lxml import html
import requests
import time
import datetime
import os
import webbrowser
# function for creating OS X notifications
def notify(title, subtitle, message, sound):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    x = '-sound {!r}'.format(sound)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s, x])))
# variable for triggering program end once new item found
found = False
# while loop to check page every 20 seconds
while(found == False):
	# request page
	page = requests.get('http://shop.yeezysupply.com/collections/men-footwear')
	# load page into tree
	tree = html.fromstring(page.content)
	# retrieve all links of class 'product-link'
	shoes = tree.xpath('//a[@class="product-link"]/@href')
	# check to see if there are still 4 shoes on the site
	if(len(shoes) == 4):
		# print the time
		print "Checked (%s)" % datetime.datetime.now().strftime('%I:%M:%S')
		# empty the variables
		page = ""
		tree = ""
		shoes = ""
		# rest for 20 seconds
		time.sleep(20)
	# if there aren't 4 shoes anymore, presumably another shoe has been added, so let me know
	else:
		# send OS X notification containing time
		notify(title = "Yeezy Bot", subtitle = "%s" % datetime.datetime.now().strftime('%I:%M:%S'), message = "Something's Changed!", sound = "Purr")
		# open the men's footwear page in default browser
		webbrowser.open('http://shop.yeezysupply.com/collections/men-footwear')
		# set found variable to true so that the while loop stops and the program ends
		found = True