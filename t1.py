import re
import os
import time
from urllib.request import Request, urlopen
import urllib 
from os import mkdir, makedirs

def get_content(site):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    content = urlopen(req).read().decode('utf-8')
    return content;



url=input('Please enter the site address:')
content= get_content(url)
print (content)