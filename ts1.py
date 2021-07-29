
import re
import os
import time
from urllib.request import Request, urlopen
import urllib
import cgi, cgitb

f=open("/Users/leonqi/content1.txt", "r")
if f.mode == 'r':
	contents =f.read()
	#print (contents)


def get_image_link(image_page):
    content=contents
    pattern = re.compile(r'img id.*?'+'\.jpg')
    match=pattern.search(content)
    image_link=match.group()
    image_link=image_link[18:]
    return image_link;




print (get_image_link(contents))